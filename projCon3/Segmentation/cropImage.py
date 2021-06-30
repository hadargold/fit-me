# Improting Image class from PIL module
from PIL import Image

def crop(path):
    # Opens a image in RGB mode
    im = Image.open(path)
    im.resize((900, 1600)).save(path)
    # im.show()

    # Setting the points for cropped image
    left = 0
    top = 350
    right = 900
    bottom = 1250

    # Cropped image of above dimension
    # (It will not change orginal image)
    im.crop((left, top, right, bottom)).save('C:\\Users\\hadar\\PycharmProjects\\projCon3\\testImg.png')

    # Shows the image in image viewer
    # im1.show()


