from PIL import Image

with Image.open('Images\\Bird.jpg') as img:
    img.load()

# img.show()
print(img.size)
print(img.format)
print(img.mode)
print(img.height)
print(img.width)

resized = img.resize((img.width // 3, img.height // 3))
# resized.show()
print(resized.size)

reduced = img.reduce(4)  # reduce size by 1/4
# reduced.show()

cropped = img.crop((400, 500, 1500, 2000))
# cropped.show()

with Image.open('Images\\Flowers.jpg') as img:
    img.load()

img.show()

img.rotate(45, expand=True).show()

mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)
mirrored.show()

reversed_img = img.transpose(Image.FLIP_TOP_BOTTOM)
reversed_img.show()