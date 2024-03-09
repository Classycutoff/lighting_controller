import numpy as np


def normalize_decibels(decibels):
    # Clip decibel values to the range [30, 100]
    decibels = np.clip(decibels, 30, 100)

    # Apply logarithmic normalization
    normalized = (
        (np.log10(decibels) - np.log10(30)) / (np.log10(100) - np.log10(30))
    ) * 255

    # Clip normalized values to the range [0, 255]
    normalized = np.clip(normalized, 0, 255)

    return normalized.astype(np.uint8)


# Example usage
decibels = np.array([25, 50, 75, 100, 105])
normalized_values = normalize_decibels(decibels)
print(normalized_values)
