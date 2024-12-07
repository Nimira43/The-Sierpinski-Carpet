import matplotlib.pyplot as plt
import numpy as np

def sierpinkski_carpet(x, y, size, depth):
  if depth == 0:
    plt.fill([x, x + size, x + size, x], [y, y, y + size, y + size], 'k')