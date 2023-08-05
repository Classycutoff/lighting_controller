import pyaudio
import struct
import tkinter as tk
import numpy as np

rectangle_len = 8


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
root.geometry("400x200")
canvas = tk.Canvas(root, width=400, height=200, bg="black")
canvas.pack()
rectangle = canvas.create_rectangle(0, 0, 400, 200, fill="black")


fft_freqs = np.fft.fftfreq(CHUNK, 1.0 / RATE)
freq_bands = np.linspace(0, len(fft_freqs) - 1, rectangle_len, dtype=int)

freq_count_band = np.linspace(20, 44100 / 2 + 1, rectangle_len, dtype=int)

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

low_range_upper_limit = 128
high_range_upper_limit = 256
low_range_list = np.linspace(0, low_range_upper_limit, 17, dtype=int)
high_range_list = np.linspace(
    low_range_upper_limit, high_range_upper_limit, 17, dtype=int
)

range_list = np.concatenate((low_range_list, high_range_list))
range_dict = {}
for i in range(len(range_list)):
    range_dict[range_list[i]] = hex_transform[i % 16]

rectangles = []
for i in range(rectangle_len):
    rectangle = canvas.create_rectangle(
        i * 50, 0, (i + 1) * 50, 200, fill="black"
    )  # Initial color is green
    rectangles.append(rectangle)


def round_to_range(range, number):
    return min(range, key=lambda x: abs(x - number))


def get_audio_freq_count(data):
    global freq_count_band
    data_np = np.array(struct.unpack(f"{CHUNK}h", data), dtype="h")
    fft_data = np.fft.fft(data_np)
    temp_freq_dict = {key: 0 for key in freq_count_band}
    for i in range(len(freq_bands) - 1):
        temp_freq_dict[
            round_to_range(
                freq_count_band,
                np.average(np.abs(fft_data[freq_bands[i] : freq_bands[i + 1]])),
            )
        ] += 1

    return temp_freq_dict


def update_bar(rectangle_obj, freq, freq_count):
    global canvas, low_range_upper_limit, high_range_upper_limit, range_list, range_dict
    if freq_count >= 8:
        fill_color_temp = hex_transform_test[3]
    else:
        fill_color_temp = hex_transform_test[freq_count % 4]
    if freq_count >= 3:
        fill_color = f"#{fill_color_temp}00"
    else:
        fill_color = f"#00{fill_color_temp}"
    canvas.itemconfig(rectangle_obj, fill=fill_color)
    # canvas.itemconfig(rectangle, fill=f"#{intensity:02x}")


def main():
    global stream
    data = stream.read(CHUNK)
    freq_count = get_audio_freq_count(data)
    print(freq_count)
    i = 0
    for key, value in freq_count.items():
        update_bar(rectangles[i], key, value)
        i += 1
    root.after(20, main)


main()

root.mainloop()
stream.stop_stream()
stream.close()
p.terminate()
