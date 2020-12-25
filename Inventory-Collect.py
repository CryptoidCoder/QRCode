#PLAN:
# Read the QRCode with the Read-Data.py script. /
# Then output that data to a table (1st column = itemname, 2nd column = number, 3rd column = in/out/broken) or .csv file
# create a app where you can create items, mark them in/out/broken, 

# App should always have a camera feed, then once a QRCode is found, have buttons for Mark in/out/broken & creating new QR codes.

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(input("What File should I open to read the QR Code from: "))
result = decode(img)
data = None
for i in result:
    data = i.data.decode("utf-8")
data = "QR-LED-000001, QR-LED-000002, QR-LED-000003"
print("data = "+ data) # data = the data from the QR Code in the form of a string

# Now need to find the word "QR" as the format for all QR-code names is "QR-Name-Number" where Name & Number change but "QR" doesn't. {This is fine for now as we only read one file at a time so there is only one dataset}
# Then need to take the line after QR out and put save it as a seperate string.

for i in range(0, len(data), 15):    
    seperated_data = (data[i:i+15])
    print(seperated_data)