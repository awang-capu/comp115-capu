from PIL import Image
img = Image.open("rick_and_morty.png")

# Convert the image to grayscale
gray_img = img.convert("L")
gray_img.show()
gray_img.save('rick_and_morty_gray.png')

img.close()
gray_img.close()