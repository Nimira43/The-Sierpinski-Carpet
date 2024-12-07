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

plt.figure(figsize=(8, 8))

# start at (0, 0) with size 1 and depth 4
sierpinkski_carpet(0, 0, 1, 4)
plt.axis('equal')
plt.axis('off')
plt.show()
