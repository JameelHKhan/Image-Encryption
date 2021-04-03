# Jameel H. Khan
# Module 8 Assignment - ImageEncrypter

from lfsr import LFSR
from PIL import Image

class ImageEncrypter:
    # class constructor method
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name # I think this is actually supposed to be the file path?: "C:/Users/Jameel/Desktop/football.png"

    # open the image by 'file_name'
    def open_image(oi, file_name: str):
        im = Image.open(oi.file_name)
        return im

    # convert the image to a 2D array of tuples of the form (R, G, B)
    def pixel_array(pix) -> list:
        imgArray = list(pix.getdata())
        return imgArray

    # encrypt the 2D array returned from pixel_array
    def transform(trsf, pixel_list: list) -> list:
        encryptedArray = []
        tempList = []
        for i in range(len(trsf.pixel_list)):
            for j in range(3):
                trsf.lfsr.step()
                binVal = bin(int( trsf.lfsr.seed, 2) ^ trsf.pixel_list[i][j])
                tempList.append(binVal)
            encryptedArray.append(tuple(tempList))
            tempList.clear()
        return encryptedArray

    # convert the encrypted 2D array back into an image name 'file_name'
    # def save_image(savige, file_name: str):


footballFilePath = "C:/Users/Jameel/Desktop/football.png"
a = LFSR("10011010", 5)     # initial LFSR object
b = ImageEncrypter(a, footballFilePath)     # ImageEncrypter object, which contains initial LFSR object & filepath
c = b.open_image(footballFilePath)          # opened image, maybe call it footballOpenedImage?
d = b.pixel_array(c)    # 2D list of original image pixel data, maybe call it footballImagePixelArray?

print(d)

# main()

'''
def main():
    footballFilePath = "C:/Users/Jameel/Desktop/football.png"
    a = LFSR("10011010", 5)     # initial LFSR object
    b = ImageEncrypter(a, footballFilePath)     # ImageEncrypter object, which contains initial LFSR object & filepath
    c = b.open_image(footballFilePath)          # opened image, maybe call it footballOpenedImage?
    d = b.pixel_array(c)    # 2D list of original image pixel data, maybe call it footballImagePixelArray?
    e = b.transform(d)      # 2D list of encrypted image pixel data
'''
