import pyaudio
import struct
import tkinter as tk


# Function to get the audio intensity
def get_audio_intensity(data):
    # Calculate the average volume of the audio samples
    rms = 0
    count = len(data) // 2
    for i in range(count):
        sample = struct.unpack("h", data[i * 2 : (i + 1) * 2])[0]
        rms += sample * sample
    rms = int((rms / count) ** 0.5)
    return rms


# Function to update the bar color
def update_bar():
    global canvas, stream
    data = stream.read(CHUNK)
    intensity = get_audio_intensity(data)
    canvas.itemconfig(rectangle, fill=f"#{intensity:02x}")
    root.after(20, update_bar)


# Set up the audio stream
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

# Create the GUI window
root = tk.Tk()
root.title("Audio Visualizer")
root.geometry("400x200")

canvas = tk.Canvas(root, width=400, height=200, bg="black")
canvas.pack()

rectangle = canvas.create_rectangle(
    0, 0, 400, 200, fill="green"
)  # Initial color is green

# Start the update loop
update_bar()

# Run the GUI loop
root.mainloop()

# Stop and close the audio stream
stream.stop_stream()
stream.close()
p.terminate()
