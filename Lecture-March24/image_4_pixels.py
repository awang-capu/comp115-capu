from PIL import Image

# Create an image of 3 by 2 (width by height)
img_pixels = Image.new('RGB', (3, 2)) 

pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (255, 255, 0), (255, 255, 0)]
img_pixels.putdata(pixels)

# # Read one pixel
# pixel_values = img_pixels.getpixel((1, 0)) # col, row
# print(f"Red: {pixel_values[0]}, green: {pixel_values[1]}, blue: {pixel_values[2]}")

# Change one pixel
img_pixels.putpixel((1, 1), (255, 0, 0))

# Save the image to an image file named pixels
img_pixels.save('/Users/alice/Desktop/six_pixels.png')

img_pixels.show()
img_pixels.close()