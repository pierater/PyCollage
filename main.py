from PIL import Image

HOR = 25
VER = 25


def main():
    im = Image.open("test.jpg")
    width, height = im.size
    print width, height
    cutBox(im)

def cutBox(im):
    startX = 0
    startY = 0
    box = (startX, startY, HOR, VER)
    region = im.crop(box)
    region.show()
    findAverageColor(region)

def findAverageColor(im):#This is all Jelly!!
    red = 0
    green = 0
    blue = 0

    x, y = im.size # gets height and width
    count = 0 

    pixels = im.load()
    for i in range(x):
        for j in range(y):
            tempr,tempg,tempb = pixels[i,j]
            red += tempr
            green += tempg
            blue += tempb
            count += 1

    avgRed = red/count
    avgGreen = green/count
    avgBlue = blue/count
    print (avgRed, avgGreen, avgBlue)
    im.show()

main()
