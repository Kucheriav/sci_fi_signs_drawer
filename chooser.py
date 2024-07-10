import os
import random
import shutil


src_dir = 'samples'
dst_dir = 'alphabet'

files = os.listdir(src_dir)
exist_files = os.listdir(dst_dir)
files1 = list(set(files) - set(exist_files))
random_files = random.sample(files1, 33 - len(exist_files) + 3)

for file in random_files:
    shutil.copy(os.path.join(src_dir, file), dst_dir)
