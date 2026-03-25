"""This is a simple image processing program - Diming"""
# Image processing: able to systematically visit 
# all of the rows and columns in the image. 
# Best way: nested iteration

from PIL import Image
img_pixels = Image.open('six_pixels.png')

for row in range(img_pixels.height):
    for col in range(img_pixels.width):
        pixel_values = img_pixels.getpixel((col, row))
        (r, g, b) = pixel_values
        (r, g, b) = (int(r / 2), int(g / 2), int(b / 2))
        img_pixels.putpixel((col, row), (r, g, b))

img_pixels.show()
img_pixels.save('/Users/alice/Desktop/six_pixels_dimmed.png')
img_pixels.close()


# Practice and understand more image processing 
# from 8.11.3.3 ActiveCode on the interactive textbook