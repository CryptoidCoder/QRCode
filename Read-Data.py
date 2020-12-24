from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(input("What File should I open to read the QR Code from: "))
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))