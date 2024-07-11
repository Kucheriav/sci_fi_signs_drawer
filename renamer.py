import os
import random
from settings import *

files = os.listdir(ALPHABET_DIR)
random.shuffle(files)
assert len(files) == len(ABC)
for i, letter in enumerate(ABC):
    os.rename(f'{ALPHABET_DIR}\\{files[i]}', f'{ALPHABET_DIR}\\{letter}.jpg')