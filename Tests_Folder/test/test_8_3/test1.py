# Test8 next success

import pyaudio
import struct
import tkinter as tk
import numpy as np

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

root = tk.Tk()
root.title("Audio Visualizer")
canvas = tk.Canvas(root, width=WIDTH, height=200, bg="pink")
canvas.pack()

# I am dividing the intensity by two, so I can get two colors (red and blue),
# and dividing all of those into 16 segments, so I can put them into hex code immediately.
hex_transform = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
]

hex_transform_test = ["4", "A", "D", "F"]

low_range_upper_limit = 22050
high_range_upper_limit = 44100
low_range_list = np.linspace(0, low_range_upper_limit, 17, dtype=int)
high_range_list = np.linspace(
    low_range_upper_limit, high_range_upper_limit, 17, dtype=int
)

range_list = np.concatenate((low_range_list, high_range_list))
range_dict = {}
for i in range(len(range_list)):
    range_dict[range_list[i]] = hex_transform[i % 16]

rectangles = []
for i in range(rectangle_amount):
    rectangle = canvas.create_rectangle(i * 50, 0, (i + 1) * 50, 200, fill="black")
    rectangles.append(rectangle)


def round_to_range(range, number):
    return min(range, key=lambda x: abs(x - number))


fft_freqs = np.fft.fftfreq(CHUNK, 1.0 / RATE)
freq_bands = np.linspace(0, len(fft_freqs) - 1, rectangle_amount + 1, dtype=int)

low_freq = 60
high_freq = 6000
freq_count_band = np.linspace(low_freq, high_freq, num=rectangle_amount, dtype=int)


def get_audio_freq_count(data):
    global freq_count_band
    data_np = np.array(struct.unpack(f"{CHUNK}h", data), dtype="h")
    fft_data = np.fft.fft(data_np)
    temp_freq_dict = {key: 0 for key in freq_count_band}
    for i in range(len(freq_count_band)):
        freq_int = int(np.average(np.abs(fft_data[freq_bands[i] : freq_bands[i + 1]])))
        temp_freq_dict[freq_count_band[i]] += freq_int

    return temp_freq_dict


def update_bar(rectangle_obj, freq, freq_int):
    global canvas, low_range_upper_limit, high_range_upper_limit, range_list, range_dict
    fill_color_temp = range_dict[round_to_range(range_list, freq_int)]
    if freq_int < low_range_upper_limit:
        fill_color = f"#{fill_color_temp}00"
    else:
        fill_color = f"#00{fill_color_temp}"
    canvas.itemconfig(rectangle_obj, fill=fill_color)
    # canvas.itemconfig(rectangle, fill=f"#{intensity:02x}")


def main():
    global stream
    try:
        data = stream.read(CHUNK)
        freq_count = get_audio_freq_count(data)
        print(freq_count)
        i = 0
        for key, value in freq_count.items():
            update_bar(rectangles[i], key, value)
            i += 1
        root.after(20, main)
    except KeyboardInterrupt as k:
        stream.stop_stream()
        stream.close()
        p.terminate()
    except Exception as e:
        stream.stop_stream()
        stream.close()
        p.terminate()


main()

root.mainloop()
stream.stop_stream()
stream.close()
p.terminate()
