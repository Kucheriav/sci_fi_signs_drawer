from PIL import Image
import os
from settings import *

filtered_text =[x for x in input().lower() if x in ABC]
n = len(filtered_text)
rows, cols = golden_rectangle(n)
img_width = SYMBOL_WIDTH * cols
img_height = (SYMBOL_HEIGHT + VERT_MARGIN) * rows
img = Image.new('RGB', (img_width, img_height), (255, 255, 255))


for i, letter in enumerate(filtered_text):
    if letter in ABC:
        symbol = Image.open(os.path.join(ALPHABET_DIR, f'{letter}.jpg'))
        x = (i % cols) * SYMBOL_WIDTH
        y = (i // cols) * (SYMBOL_HEIGHT + VERT_MARGIN)
        img.paste(symbol, (x, y))

img.save('encrypted_text.jpg')