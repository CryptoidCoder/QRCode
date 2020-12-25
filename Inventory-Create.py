# This is a script to create Qr code labels for inventory.

#imports
import csv
print("")
print("Each individual item will have a different ID number.")
print("")
number =  int(input("What number should I start with: "))
number = '%06d' % number
print("New number after the change is: "+ number)
print("")

itemname = input("What is the item called: ")
print("")

numberofitems = int(input("How many Are there: "))
print("")

#creating the .csv file to make from
with open('Name&Number.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(numberofitems):
        name = "QR-" + itemname + "-" + number
        filewriter.writerow([name, number])
        number = int(number) + 1
        number = '%06d' % number
