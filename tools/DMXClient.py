import win32pipe, win32file
import json


def DMXServerError(Exception):
    raise Exception


class DMXClient:

    def __init__(self, pipeName):
        self.connected = False
        self.pipe = win32pipe.CreateNamedPipe(
            r"\\.\pipe\\" + pipeName,
            win32pipe.PIPE_ACCESS_OUTBOUND,
            win32pipe.PIPE_TYPE_MESSAGE
            | win32pipe.PIPE_READMODE_MESSAGE
            | win32pipe.PIPE_WAIT,
            win32pipe.PIPE_UNLIMITED_INSTANCES,
            65536,
            65536,
            0,
            None,
        )

    def connect(self):
        print("Waiting for connection to DMXServer...", end="", flush=True)

        win32pipe.ConnectNamedPipe(self.pipe, None)
        self.connected = True
        print("\nConnected.")

    def close(self):
        if not self.connected:
            print("Not connected.")
            return False

        win32file.CloseHandle(self.pipe)
        self.pipe.close()
        self.connected = False
        print("Connection closed.")

    def write_DMX(self, DMX_dict):
        if type(DMX_dict) != dict:
            raise ValueError("write_DMX only accepts dictionaries.")
        if not self.connected:
            raise ValueError("Not connected to DMXServer")

        PipeCommand = "DMX"
        for key, value in DMX_dict.items():
            PipeCommand += " " + str(key) + " " + str(value)

        # I don't know why, but the pipeline ignores every second write, so i write two times.
        win32file.WriteFile(self.pipe, PipeCommand.encode() + b"\n")
        # win32file.WriteFile(self.pipe, PipeCommand.encode() + b"\n")
