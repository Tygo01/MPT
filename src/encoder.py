from PIL import Image
import numpy as np
from scipy.io.wavfile import write

# C:\Users\113977\Downloads\t.png
# C:\Users\113977\Downloads\test.wav

class Encoder:
    def encode(self, imageLocation, outputLocation):
        img = Image.open(imageLocation)
        img = img.convert("L")  # Convert the image to grayscale

        pixel_values = np.array(img.getdata())
        # Normalize the pixel values to be between 0 and 1
        normalized_pixels = (pixel_values + 1)/255.0

        sample_rate = 44100
        duration = 1
        t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
        fr = []

        for x in np.nditer(normalized_pixels):
            fr.append(x * 8000)

        frequencies = np.array(fr)

        waves = np.zeros_like(t)
        for freq in frequencies:
            waves += 1.0 * np.sin(2 * np.pi * freq * t)

        waves /= np.max(np.abs(waves))
        waves = np.int16(waves * 32767)

        print(waves)

        write(outputLocation, sample_rate, waves)