from PIL import Image
import sys

images = []

for arg in sys.argv[1:]:
    image = (Image.open(arg))
    images.append(image)

images[0].save("costumes.gif", save_all=True, append_images=images[1:], optimize=False, duration=400, loop=0)

