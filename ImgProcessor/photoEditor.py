from PIL import Image, ImageEnhance, ImageFilter
import os

path="./imgs"
pathOut = "./editedImgs"

for filename in os.listdir(path):
    # holds image variable
    img = Image.open(f"{path}/{filename}")
    # applies edits to photos
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')


