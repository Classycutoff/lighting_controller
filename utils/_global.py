from pyaudio import paInt16

AUDIO_CHUNK = 1024 * 2
AUDIO_FORMAT = paInt16
AUDIO_CHANNELS = 1
AUDIO_RATE = 44100

START_FREQ = 20
END_FREQ = 4000
NUM_FREQ_CHUNKS = 8

DB_MIN = 15
DB_MAX = 125

COLOR_BINS = [0, 50, 100, 150, 200, 255]

COLORS_TO_BINS = {
    1: {"R": 255, "G": 0, "B": 0},  # Red
    2: {"R": 128, "G": 0, "B": 128},  # Purple
    3: {"R": 0, "G": 0, "B": 255},  # Blue
    4: {"R": 0, "G": 255, "B": 255},  # Yellow
    5: {"R": 255, "G": 255, "B": 255},  # white
}

slow_dimming_chan = {}
