from PIL import Image

left = int(input('pixels from left: '))
upper = int(input('pixels from upper: '))
right = int(input('pixels from right: '))
lower = int(input('pixels from down: '))
img_path = str(input('input path to the image: '))

open_img = Image.open(img_path)
crop_image = open_img.crop((left,upper,right,lower))
crop_image.show()