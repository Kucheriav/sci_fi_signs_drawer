from PIL import Image, ImageDraw
import os
import math


def golden_rectangle(area):
    # Золотое сечение
    phi = (1 + math.sqrt(5)) / 2

    # Найдем длину стороны квадрата
    side_square = math.sqrt(area)

    # Найдем длину короткой стороны прямоугольника
    short_side = math.ceil(side_square / phi)

    # Найдем длину длинной стороны прямоугольника
    long_side = math.ceil(short_side * phi)

    return short_side, long_side




img_dir = 'alphabet'
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input().lower()
filtered_text = ''
for el in text:
    if el in letters:
        filtered_text += el

n = len(filtered_text)

rows = cols = 0
# for rows in range(int(n ** 0.5), 1, -1):
#     if n % rows == 0:
#         cols = n // rows
#         break
# print(cols, rows)
rows, cols = golden_rectangle(n)

char_width = 90
char_height = 60
vert_margin = 15
img_width = char_width * cols
img_height = (char_height + vert_margin) * rows
img = Image.new('RGB', (img_width, img_height), (255, 255, 255))


for i, letter in enumerate(filtered_text):
    if letter in letters:
        char = Image.open(os.path.join(img_dir, f'{letter}.jpg'))
        x = (i % cols) * char_width
        y = (i // cols) * (char_height + vert_margin)
        img.paste(char, (x, y))

img.save('encrypted_text.jpg')