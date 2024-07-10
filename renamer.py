import os
import random

dst_dir = 'alphabet'
files = os.listdir(dst_dir)
random.shuffle(files)
abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
assert len(files) == len(abc)
for i, letter in enumerate(abc):
    os.rename(f'{dst_dir}\\{files[i]}', f'{dst_dir}\\{letter}.jpg')