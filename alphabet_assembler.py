import os
from PIL import Image, ImageDraw, ImageFont

# Папка с картинками
img_dir = 'alphabet'

img_width, img_height = 90, 60
letter_size = 60
hor_margin = 10
vert_margin = 10
result_img = Image.new('RGB', ((img_width + letter_size + hor_margin) * 3, (img_height + vert_margin) * 11), (255, 255, 255))

font = ImageFont.truetype('arial.ttf', 40)
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()

# Список файлов картинок
img_files = os.listdir(img_dir)
print(img_files)

for i, letter in enumerate(letters):
    img = Image.open(os.path.join(img_dir, f'{letter}.jpg'))
    x = (i % 3) * (img_width + letter_size + hor_margin)
    y = (i // 3) * (img_height + vert_margin)
    result_img.paste(img, (x, y))
    draw = ImageDraw.Draw(result_img)
    draw.text((x + img_width + hor_margin, y), letters[i], font=font, fill=(0, 0, 0))
result_img.save('res.jpg')