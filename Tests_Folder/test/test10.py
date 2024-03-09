import pyaudio
import struct
import tkinter as tk


# Set up the audio stream
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

smooth_temp = 0

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)


def get_audio_intensity(data):
    # Calculate the average volume of the audio samples
    rms = 0
    count = len(data) // 2
    for i in range(count):
        sample = struct.unpack("h", data[i * 2 : (i + 1) * 2])[0]
        rms += sample * sample
    rms = int((rms / count) ** 0.5)
    return rms


while True:
    data = stream.read(CHUNK)
    intensity = get_audio_intensity(data)
    print(intensity)
