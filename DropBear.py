import numpy as np
import matplotlib.pyplot as plt

#Declaring the size of the simulation area
width = 200
height = 200

grid = np.zeros((height, width))
print(grid) #For errors

#To Visualize the grid
plt.imshow(grid, origin='lower', cmap='binary')
plt.title("200x200 Monitoring Grid")
plt.xticks([])  
plt.yticks([])  
plt.grid(False)


plt.show()