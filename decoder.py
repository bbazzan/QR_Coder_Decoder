from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(input('Enter the path to the QR Code to decode: '))

result = decode(img)

print(result)
