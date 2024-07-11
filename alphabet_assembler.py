import os
from PIL import Image, ImageDraw, ImageFont
from settings import *


img_files = os.listdir(ALPHABET_DIR)
result_img = Image.new('RGB', ((SYMBOL_WIDTH + LETTER_SIZE + HOR_MARGIN) * 3,
                               (SYMBOL_HEIGHT + VERT_MARGIN) * 11), (255, 255, 255))
draw = ImageDraw.Draw(result_img)
font = ImageFont.truetype('arial.ttf', 40)
letters = ABC.upper()

for i, letter in enumerate(letters):
    img = Image.open(os.path.join(ALPHABET_DIR, f'{letter}.jpg'))
    x = (i % 3) * (SYMBOL_WIDTH + LETTER_SIZE + HOR_MARGIN)
    y = (i // 3) * (SYMBOL_HEIGHT + VERT_MARGIN)
    result_img.paste(img, (x, y))
    draw.text((x + SYMBOL_WIDTH + HOR_MARGIN, y), letters[i], font=font, fill=(0, 0, 0))
result_img.save('алфавит.jpg')