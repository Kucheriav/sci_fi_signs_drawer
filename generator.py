from PIL import Image, ImageDraw
import itertools
import os
# Размер целевой картинки
width, height = 90, 60

# Координаты вершин квадрата
vertices = [(10, 10), (40, 10), (70, 10), (10, 40), (40, 40), (70, 40)]



# Генерируем все возможные комбинации вершин
c = 1
for r in range(3, 8):
    for points in itertools.permutations(vertices, r):
        img = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.line(points, fill=(0, 0, 0), width=2)
        img.save(f'samples\polyline_combinations{c}.png')
        c += 1

