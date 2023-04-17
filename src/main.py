from encoder import Encoder

testEncoder = Encoder()

inputImage = input("Enter the path to the image you want to encode: ")
outputPath = input("Enter the path to the output file: ")

testEncoder.encode(inputImage, outputPath)