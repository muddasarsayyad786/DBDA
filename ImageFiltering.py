from PIL import Image, ImageFilter

with Image.open('Images\\buildings.jpg') as img:
    img.load()

img.show()

blurred = img.filter(ImageFilter.BLUR)
blurred.crop((200, 300, 800, 600)).show()

blurred = img.filter(ImageFilter.BoxBlur(10))
blurred.crop((200, 300, 800, 600)).show()

blurred = img.filter(ImageFilter.GaussianBlur(5))
blurred.crop((200, 300, 800, 600)).show()

edges = img.filter(ImageFilter.FIND_EDGES)
enhanced_edges = edges.filter(ImageFilter.EDGE_ENHANCE)
enhanced_edges.crop((200, 300, 800, 600)).show()

smooth_edges = edges.filter(ImageFilter.SMOOTH)
smooth_edges.crop((200, 300, 800, 600)).show()

embossed = img.filter(ImageFilter.EMBOSS)
embossed.show()
