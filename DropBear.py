import numpy as np
import matplotlib.pyplot as plt

width = 200
height = 200

grid = np.zeros((height, width))
print(grid)
plt.imshow(grid, origin='lower', cmap='binary')
plt.title("100x100 Monitoring Grid")
plt.xticks([])  # removes x-axis numbers
plt.yticks([])  # removes y-axis numbers

plt.grid(False)


plt.show()