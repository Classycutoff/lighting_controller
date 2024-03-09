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

low_range_upper_limit = 750
high_range_upper_limit = 3500
low_range_list = np.linspace(0, low_range_upper_limit + 1, 17, dtype=int)
high_range_list = np.linspace(
    low_range_upper_limit, high_range_upper_limit + 1, 17, dtype=int
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


def round_to_range(number):
    global range_list
    return min(range_list, key=lambda x: abs(x - number))


def get_audio_intensity(data):
    # Apply FFT to the audio data
    data_np = np.array(struct.unpack(f"{CHUNK}h", data), dtype="h")
    fft_data = np.fft.fft(data_np)
    fft_freqs = np.fft.fftfreq(CHUNK, 1.0 / RATE)

    # Divide the frequency spectrum into 8 bands
    freq_bands = np.linspace(0, len(fft_freqs) - 1, rectangle_len + 1, dtype=int)
    temp_intensities = [
        round_to_range(np.average(np.abs(fft_data[freq_bands[i] : freq_bands[i + 1]])))
        for i in range(rectangle_len)
    ]
    print(temp_intensities)

    # Normalize the intensities to fit in the 0-255 range for color representation
    intensities = [
        intensity.astype(int)
        for intensity in (temp_intensities / np.max(temp_intensities) * 255)
    ]
    return intensities


def update_bar(rectangle_obj, intensity):
    global canvas, low_range_upper_limit, high_range_upper_limit
    rounded_intensity = round_to_range(intensity)
    if rounded_intensity >= 250:
        canvas.itemconfig(rectangle_obj, fill=f"#{range_dict[rounded_intensity]}00")
    else:
        canvas.itemconfig(rectangle_obj, fill=f"#00{range_dict[rounded_intensity]}")
    # canvas.itemconfig(rectangle, fill=f"#{intensity:02x}")


def main():
    global stream
    data = stream.read(CHUNK)
    intensities = get_audio_intensity(data)
    print(intensities)
    for i in range(len(rectangles)):
        update_bar(rectangles[i], intensities[i])
    root.after(20, main)


main()

root.mainloop()
stream.stop_stream()
stream.close()
p.terminate()
