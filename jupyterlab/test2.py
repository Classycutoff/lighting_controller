# Test8 next success

import pyaudio
import struct
import tkinter as tk
import numpy as np

import scipy.io.wavfile as wavfile
import numpy as np
import pylab as pl

# Variables
WIDTH = 400
rectangle_amount = 8

# Set up the audio stream
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)
