import pyaudio
import struct
import tkinter as tk
import numpy as np


# Function to get the audio intensity
def get_audio_intensity(data):
    # Apply FFT to the audio data
    data_np = np.array(struct.unpack(f"{CHUNK}h", data), dtype="h")
    fft_data = np.fft.fft(data_np)
    fft_freqs = np.fft.fftfreq(CHUNK, 1.0 / RATE)

    # Divide the frequency spectrum into 8 bands
    freq_bands = np.linspace(0, len(fft_freqs) - 1, 9, dtype=int)
    intensities = [
        np.average(np.abs(fft_data[freq_bands[i] : freq_bands[i + 1]]))
        for i in range(8)
    ]

    # Normalize the intensities to fit in the 0-255 range for color representation
    intensities = [
        intensity.astype(int) for intensity in (intensities / np.max(intensities) * 255)
    ]
    return intensities


# Function to update the bar colors
def update_bars():
    global canvas, stream
    data = stream.read(CHUNK)
    intensities = get_audio_intensity(data)

    for i, intensity in enumerate(intensities):
        color = f"#{intensity:02x}{255 - intensity:02x}00"
        canvas.itemconfig(rectangles[i], fill=color)

    root.after(20, update_bars)


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

rectangles = []
for i in range(8):
    rectangle = canvas.create_rectangle(
        i * 50, 0, (i + 1) * 50, 200, fill="green"
    )  # Initial color is green
    rectangles.append(rectangle)

# Start the update loop
update_bars()

# Run the GUI loop
root.mainloop()

# Stop and close the audio stream
stream.stop_stream()
stream.close()
p.terminate()
