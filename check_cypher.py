from PIL import Image, ImageDraw, ImageFont
from settings import *


font = ImageFont.truetype('arial.ttf', 40)
filtered_text =[x for x in input().lower() if x in ABC]
n = len(filtered_text)
rows, cols = golden_rectangle(n)
img_width = LETTER_SIZE * cols
img_height = (LETTER_SIZE + VERT_MARGIN) * rows
img = Image.new('RGB', (img_width, img_height), (255, 255, 255))
draw = ImageDraw.Draw(img)

for i, letter in enumerate(filtered_text):
    x = (i % cols) * LETTER_SIZE
    y = (i // cols) * (LETTER_SIZE + VERT_MARGIN)
    draw.text((x, y), letter, font=font, fill=(0, 0, 0))
img.save('test_text.jpg')