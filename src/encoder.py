from PIL import Image

class Encoder:
    def encode(self, imageLocation, outputLocation):
        img = Image.open(imageLocation)
        img = img.convert("L")  # Convert the image to grayscale

        pixel_values = list(img.getdata())
        # Normalize the pixel values to be between 0 and 1
        normalized_values = [x / 255.0 for x in pixel_values]
        # Reshape the normalized pixel values into a 2D array
        width, height = img.size
        normalized_pixels = [normalized_values[i:i + width] for i in range(0, len(normalized_values), width)]
        print(normalized_pixels)