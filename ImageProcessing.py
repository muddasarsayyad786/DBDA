from PIL import Image
import numpy as np

zeros = np.zeros((600,600))
my_img = Image.fromarray(zeros)
my_img.show()

zeros[200:400, 200:400] = 255
my_img = Image.fromarray(zeros)
my_img.show()

r_zeros = np.zeros((600,600))
r_zeros[:200] = 255
red_band = Image.fromarray(r_zeros).convert('L')

g_zeros = np.zeros((600,600))
g_zeros[200:400] = 255
green_band = Image.fromarray(g_zeros).convert('L')

b_zeros = np.zeros((600,600))
b_zeros[400:] = 255
blue_band = Image.fromarray(b_zeros).convert('L')

my_image = Image.merge("RGB", (red_band, green_band, blue_band))
my_image.show()