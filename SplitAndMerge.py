from PIL import Image
import numpy as np

with Image.open('Images\\Strawberry.jpg') as img:
    img.load()

img.show()

# grayed = img.convert('L')
# grayed.show()

print(img.getbands())

red, green, blue = img.split()

zero_band = red.point(lambda _: 0)

# red_image = Image.merge("RGB", (red, zero_band, zero_band))
# red_image.show()
#
# green_image = Image.merge("RGB", (zero_band, green, zero_band))
# green_image.show()
#
# blue_image = Image.merge("RGB", (zero_band, zero_band, blue))
# blue_image.show()

resized = img.resize((img.width // 4, img.height // 4))
arr = np.array(resized)
print(arr[50, 100])


