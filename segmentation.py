# from: https://www.youtube.com/watch?v=W-oVad7x-HQ

import cv2
from matplotlib import pyplot as plt
import requests
from PIL import Image, ImageOps


img2 = Image.open("try.jpg")
img2.resize((100, 100)).save('tryNew.jpg')

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('tryNew.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': '5DdEQPfrPieHM9FCq4CzN3oF'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)


im = Image.open('no-bg.png').convert('RGB')
im_invert = ImageOps.invert(im)
im_invert.save('no-bg.png')

img = cv2.imread("no-bg.png")

img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 253, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret, thresh3 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)


print(ret)

plt.figure("BINARY")
plt.imshow(thresh, cmap ='gray')

plt.axis('off')

plt.savefig('seg.jpg')
image = Image.open(r'C:\Users\hadar\PycharmProjects\ENet_human_part_segmentation-master\segmentation_final\seg.jpg')
image.resize((100, 100)).save('finalPic.png')

plt.figure("Grayscale")
plt.imshow(gray, cmap ='gray')

plt.show()
