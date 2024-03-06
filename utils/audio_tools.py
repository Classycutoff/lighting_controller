import pyaudio
import struct
import numpy as np
import sounddevice as sd

import utils._global as _global
from effects.audio_dmx import *


def find_device_index() -> int:
    device_list = sd.query_devices()
    for device in device_list:
        if "VoiceMeeter Output (VB-Audio Vo" == device["name"]:  # type: ignore
            return device["index"]  # type: ignore
    else:
        print("Define Audio didnt find voicemeeter output")
        raise ValueError


def divide_frequency_range_into_chunks(start_freq, end_freq, num_chunks):
    frequencies = np.logspace(
        np.log10(start_freq), np.log10(end_freq), num=num_chunks, base=10, endpoint=True
    )
    frequency_chunks = [frequencies[i] for i in range(num_chunks)]
    return frequency_chunks


def divide_frequency_spectrum_into_logarithmic_chunks(
    spectrum, logspace_frequencies, chunks
):
    frequencies = np.fft.fftfreq(len(spectrum), 1 / _global.AUDIO_RATE)
    pos_frequencies = frequencies[: len(frequencies) // 2]
    chunk_indices = np.searchsorted(pos_frequencies, logspace_frequencies)
    frequency_chunks = [
        spectrum[chunk_indices[i] : chunk_indices[i + 1]] for i in range(chunks)
    ]
    frequency_chunks.append(spectrum[chunk_indices[chunks] :])
    return frequency_chunks


def calculate_loudness(data):
    spectrum = np.fft.fft(data)
    magnitude = np.abs(spectrum)

    return magnitude


def calculate_loudness_of_freq_chunk(freq_chunks):
    loudness = [np.mean(chunk) for chunk in freq_chunks if chunk.size > 0]
    return loudness


def define_stream():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=_global.AUDIO_FORMAT,
        channels=_global.AUDIO_CHANNELS,
        rate=_global.AUDIO_RATE,
        input=True,
        output=True,
        frames_per_buffer=_global.AUDIO_CHUNK,
        input_device_index=find_device_index(),
    )
    return stream


def get_audio_stream(stream=False, divided_freq_chunks=False):
    if not stream:
        stream = define_stream()
        divided_freq_chunks = divide_frequency_range_into_chunks(
            start_freq=_global.START_FREQ,
            end_freq=_global.END_FREQ,
            num_chunks=_global.NUM_FREQ_CHUNKS,
        )

    data = stream.read(_global.AUDIO_CHUNK)  # type: ignore
    data_array = np.frombuffer(data, dtype=np.int16)
    spectrum = calculate_loudness(data_array)

    frequency_chunks = divide_frequency_spectrum_into_logarithmic_chunks(
        spectrum, divided_freq_chunks, _global.NUM_FREQ_CHUNKS - 1
    )
    loudness = calculate_loudness_of_freq_chunk(frequency_chunks)
    # colors = plt.cm.viridis(normalized_loud)  # Use colormap to represent volume levels

    dmx_values = audio_to_dmx(loudness)

    result = []
    result.append((stream, divided_freq_chunks))
    result.append(dmx_values)

    return result
