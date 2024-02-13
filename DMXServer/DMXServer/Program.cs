using System;
using System.Runtime.InteropServices;
using System.IO;
using System.IO.Pipes;
using System.Threading;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Remoting.Channels;
//using Newtonsoft.Json;

namespace DMX_Server
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Assigning values.
            var pipeName = "DMX_Pipe";
            List<int> DMX_Channel_List = new List<int>();
            List<byte> DMX_Value_List = new List<byte>();


            // Open connection to the OpenDMX device.
            try
            {
                OpenDMX.start();
                if (OpenDMX.status == FT_STATUS.FT_DEVICE_NOT_FOUND)
                    Console.WriteLine("No Enttec USB Device Found");
                else if (OpenDMX.status == FT_STATUS.FT_OK)
                    Console.WriteLine("Found an Enttec USB DMX Device.");
                else
                    Console.WriteLine("Error Opening Device");
            }
            catch (Exception exp)
            {
                Console.WriteLine(exp);
                Console.WriteLine("Error Connecting to Enttec USB Device");

            }


            // Opening the Pipeline to the python code.
            // It connects based on the pipeName.
            while (true)
            {
                    using (NamedPipeClientStream pipeClient =
                   new NamedPipeClientStream(".", pipeName, PipeDirection.In))
                {

                    Console.WriteLine("Waiting for connection to DMXClient...");
                    pipeClient.Connect();
                    Console.WriteLine("Connected");
                    using (StreamReader sr = new StreamReader(pipeClient))
                    {
                        //string raw_json;
                        string input;

                        do
                        {
                            //variables used for command handling
                            //raw_json = sr.ReadLine(); //Holds the string recieved over the named pipe
                            input = sr.ReadLine();

                            if (sr.ReadLine() == null)
                            {
                                break;
                            }
                            //var input = JsonConvert.DeserializeObject<raw_json>(raw_json);
                            Console.WriteLine(input);

                            formatPipeOutput(input);
                        } while (pipeClient.IsConnected);

                        Console.WriteLine("Pipeline Disconnected.");


                    }
                    
                }

                if (false)
                {
                    Console.WriteLine("This is the stopping point");
                    break;
                }
            }

            Environment.Exit(Environment.ExitCode);
        }

        static void formatPipeOutput(string input)
        {
            int channel;
            byte value;

            List<int> DMX_Channel_List = new List<int>();
            List<byte> DMX_Value_List = new List<byte>();
            Dictionary<int, byte> DMX_Channel_Dict = new Dictionary<int, byte>();

            if (input.StartsWith("DMX "))
            { // 'DMX ...'

                string[] dmxCommand = input.Split();

                for (int i = 1; i < ((dmxCommand.Length - 1) / 2) + 1; i++)
                {
                    channel = Int16.Parse(dmxCommand[i * 2 - 1]); //Channel
                    value = byte.Parse(dmxCommand[i * 2]); //Value


                    //Console.WriteLine("{0} -> Val1: {1}, Val2: {2}", i, val1, val2);
                    if (channel < 0 || channel > 513 || value < 0 || value > 255)
                    {
                        throw new Exception();
                    }
                    DMX_Channel_List.Add(channel);
                    DMX_Channel_Dict.Add(channel, value);
                }
                changeDMX(DMX_Channel_List, DMX_Channel_Dict);


            }
        }

        static void changeDMX(List<int> DMX_Channels, Dictionary<int, byte> DMX_Channel_Dict)
        {
            for (int i = 0; i < DMX_Channels.Count; i++)
            {
                OpenDMX.setDmxValue(DMX_Channels[i], DMX_Channel_Dict[DMX_Channels[i]]);
            }
            OpenDMX.writeData();
            Thread.Sleep(5);
        }
    }

    public class OpenDMX
    {

        public static byte[] buffer = new byte[513];
        public static uint handle;
        public static bool done = false;
        public static bool Connected = false;
        public static int bytesWritten = 0;
        public static FT_STATUS status;

        public const byte BITS_8 = 8;
        public const byte STOP_BITS_2 = 2;
        public const byte PARITY_NONE = 0;
        public const UInt16 FLOW_NONE = 0;
        public const byte PURGE_RX = 1;
        public const byte PURGE_TX = 2;


        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_Open(UInt32 uiPort, ref uint ftHandle);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_Close(uint ftHandle);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_Read(uint ftHandle, IntPtr lpBuffer, UInt32 dwBytesToRead, ref UInt32 lpdwBytesReturned);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_Write(uint ftHandle, IntPtr lpBuffer, UInt32 dwBytesToRead, ref UInt32 lpdwBytesWritten);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_SetDataCharacteristics(uint ftHandle, byte uWordLength, byte uStopBits, byte uParity);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_SetFlowControl(uint ftHandle, char usFlowControl, byte uXon, byte uXoff);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_GetModemStatus(uint ftHandle, ref UInt32 lpdwModemStatus);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_Purge(uint ftHandle, UInt32 dwMask);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_ClrRts(uint ftHandle);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_SetBreakOn(uint ftHandle);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_SetBreakOff(uint ftHandle);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_GetStatus(uint ftHandle, ref UInt32 lpdwAmountInRxQueue, ref UInt32 lpdwAmountInTxQueue, ref UInt32 lpdwEventStatus);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_ResetDevice(uint ftHandle);
        [DllImport("FTD2XX.dll")]
        public static extern FT_STATUS FT_SetDivisor(uint ftHandle, char usDivisor);


        public static void start()
        {
            handle = 0;
            status = FT_Open(0, ref handle);
            //setting up the WriteData method to be on it's own thread. This will also turn all channels off
            //this unrequested change of state can be managed by getting the current state of all channels 
            //into the write buffer before calling this function.
            Thread thread = new Thread(new ThreadStart(writeData));
            thread.Start();
        }

        public static void setDmxValue(int channel, byte value)
        {
            if (buffer != null)
            {
                buffer[channel] = value;
            }
        }

        public static void writeData()
        {
            try
            {
                initOpenDMX();
                if (OpenDMX.status == FT_STATUS.FT_OK)
                {
                    status = FT_SetBreakOn(handle);
                    status = FT_SetBreakOff(handle);
                    bytesWritten = write(handle, buffer, buffer.Length);

                    Thread.Sleep(1);      //give the system time to send the data before sending more 

                    Array.Clear(buffer, 0, buffer.Length);      // Clear the buffer before writing more.
                }
            }
            catch (Exception exp)
            {
                Console.WriteLine(exp);
            }

        }

        public static int write(uint handle, byte[] data, int length)
        {
            try
            {
                IntPtr ptr = Marshal.AllocHGlobal((int)length);
                Marshal.Copy(data, 0, ptr, (int)length);
                uint bytesWritten = 0;
                status = FT_Write(handle, ptr, (uint)length, ref bytesWritten);
                return (int)bytesWritten;
            }
            catch (Exception exp)
            {
                Console.WriteLine(exp);
                return 0;
            }
        }

        public static void initOpenDMX()
        {
            status = FT_ResetDevice(handle);
            status = FT_SetDivisor(handle, (char)12);  // set baud rate
            status = FT_SetDataCharacteristics(handle, BITS_8, STOP_BITS_2, PARITY_NONE);
            status = FT_SetFlowControl(handle, (char)FLOW_NONE, 0, 0);
            status = FT_ClrRts(handle);
            status = FT_Purge(handle, PURGE_TX);
            status = FT_Purge(handle, PURGE_RX);
        }

    }

    /// <summary>
    /// Enumaration containing the varios return status for the DLL functions.
    /// </summary>
    public enum FT_STATUS
    {
        FT_OK = 0,
        FT_INVALID_HANDLE,
        FT_DEVICE_NOT_FOUND,
        FT_DEVICE_NOT_OPENED,
        FT_IO_ERROR,
        FT_INSUFFICIENT_RESOURCES,
        FT_INVALID_PARAMETER,
        FT_INVALID_BAUD_RATE,
        FT_DEVICE_NOT_OPENED_FOR_ERASE,
        FT_DEVICE_NOT_OPENED_FOR_WRITE,
        FT_FAILED_TO_WRITE_DEVICE,
        FT_EEPROM_READ_FAILED,
        FT_EEPROM_WRITE_FAILED,
        FT_EEPROM_ERASE_FAILED,
        FT_EEPROM_NOT_PRESENT,
        FT_EEPROM_NOT_PROGRAMMED,
        FT_INVALID_ARGS,
        FT_OTHER_ERROR
    };
}
