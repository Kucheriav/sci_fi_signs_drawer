import os
import random
import shutil
from settings import *


files = os.listdir(SAMPLES_DIR)
exist_files = os.listdir(ALPHABET_DIR)
files1 = list(set(files) - set(exist_files))
random_files = random.sample(files1, int((33 - len(exist_files)) * 1.5))
for file in random_files:
    shutil.copy(os.path.join(SAMPLES_DIR, file), ALPHABET_DIR)
