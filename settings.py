VERTICES = [(10, 10), (40, 10), (70, 10), (10, 40), (40, 40), (70, 40)]

SAMPLES_DIR = 'samples'
ALPHABET_DIR = 'alphabet'
ABC = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
HOR_MARGIN = 10
VERT_MARGIN = 15
SYMBOL_WIDTH, SYMBOL_HEIGHT = 90, 60
LETTER_SIZE = 60

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
    short_side = math.ceil(area / long_side)
    return short_side, long_side