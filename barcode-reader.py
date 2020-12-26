from pyzbar import pyzbar
import cv2


def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    global obj
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image


def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image


if __name__ == "__main__":
    from glob import glob

    #barcodes = glob("QR-Codes/qr1.png")
    barcodes = glob(input("What QR codes should I use (Please give the Directory e.g QR-Codes/qr1.png): "))
    for barcode_file in barcodes:
        # load the image to opencv
        img = cv2.imread(barcode_file)
        # decode detected barcodes & get the image
        # that is drawn
        img = decode(img)
        # show the image
        cv2.imshow("Read Data", img)
        # cv2.imwrite("barcode_detected.png", img)
        cv2.waitKey(0)