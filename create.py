import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

while True: # need to change this so that it asks you what type of data to add (link, text) and if it is link put it at the end.
    answer = input("Would you like to add a Dataset Y/N: ")
    if answer == 'Y' or answer == 'y':
        qr.add_data(input("Input DataSet Here: "))
        qr.add_data(" , ")

    else:
        break

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QRCode-Output.png")