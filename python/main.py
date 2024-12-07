import matplotlib.pyplot as plt
import numpy as np

def sierpinkski_carpet(x, y, size, depth):
  if depth == 0:
    plt.fill([x, x + size, x + size, x], [y, y, y + size, y + size], 'k')
  else:
    new_size = size / 3
    for i in range(3):
      for j in range(3):
        if i == 1 and j == 1:
          continue
        sierpinkski_carpet(x + i * new_size, y + j * new_size, new_size, depth - 1)