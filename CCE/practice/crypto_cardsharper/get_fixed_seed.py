
import random
import sys

card = [i for i in range(52)]
sorted_card = [i for i in range(52)]

for seed in range(-sys.maxsize - 1, sys.maxsize + 1):
    random.seed(seed)
    random.shuffle(card)

    if card == sorted_card:
        break

    card = [i for i in range(52)]
    if seed % 10000000 == 0:
        print(f'finding {seed}...')

print(seed)