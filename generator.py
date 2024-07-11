from PIL import Image, ImageDraw
from settings import *
import itertools


c = 1
for r in range(3, 8):
    for points in itertools.permutations(VERTICES, r):
        img = Image.new('RGB', (SYMBOL_WIDTH, SYMBOL_HEIGHT), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.line(points, fill=(0, 0, 0), width=2)
        img.save(f'{SAMPLES_DIR}\polyline_combinations{c}.png')
        c += 1

