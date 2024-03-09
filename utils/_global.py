from pyaudio import paInt16
import tkinter as tk

from utils.DMXClient import DMXClient

dmxClient = DMXClient("DMX_Pipe")
root = tk.Tk()

AUDIO_CHUNK = 1024 * 2
AUDIO_FORMAT = paInt16
AUDIO_CHANNELS = 1
AUDIO_RATE = 44100

START_FREQ = 20
END_FREQ = 4000
NUM_FREQ_CHUNKS = 8

DB_MIN = 15
DB_MAX = 125

COLOR_BINS = [0, 80, 110, 140, 170, 255]

COLORS_TO_BINS = {
    1: {"R": 0, "G": 128, "B": 0},
    2: {"R": 128, "G": 0, "B": 0},
    3: {"R": 0, "G": 0, "B": 128},
    4: {"R": 0, "G": 255, "B": 255},
    5: {"R": 255, "G": 255, "B": 255},
}

is_on = False
slow_dimming_chan = {}
stream, divided_freq_chunks = (False, False)

result_dmx_dict = {}
