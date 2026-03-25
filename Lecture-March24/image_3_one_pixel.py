from PIL import Image

img = Image.new('RGB', (1, 1), color = 'red')
#img = Image.new('RGB', (1, 1), (255, 0, 255))
#img = Image.new('RGB', (1, 1), (0, 0, 0))

# Save the image to an image file named one_pixel
# img.save('/Users/alice/Desktop/one_pixel_2026.png')
img.save('one_pixel_red.png')

img.show()
img.close()