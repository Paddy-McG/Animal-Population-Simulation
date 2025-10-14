import numpy as np
import matplotlib.pyplot as plt

#Declaring the size of the simulation area
width = 200
height = 200

grid = np.zeros((height, width))
print(grid) #For errors
camera_positions = np.random.rand(3, 2) * [width, height]
#To Visualize the grid
detect_radius = 25.0
fig, ax1 = plt.subplots(figsize=(6, 6))  


for i, (x, y) in enumerate(camera_positions):
    ax1.scatter(x, y, color='red', marker='^', s=100, label='Camera' if i==0 else "")
    circle = plt.Circle((x, y), detect_radius, color='black', fill=False, alpha=1, linewidth=2)
    ax1.add_patch(circle)
    ax1.text(x+2, y+2, f"C{i}", color='red', fontsize=9)
plt.show()