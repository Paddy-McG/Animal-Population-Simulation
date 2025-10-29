import numpy as np
import matplotlib.pyplot as plt

def detectAnimal(position, x, y, radius, cam, capturedCount, totalCaptured):
    dist = np.sqrt((position[:, 0] - x)**2 + (position[:, 1] - y)**2)
    captured = dist <= radius
    count = np.sum(captured)
    capturedCount[cam] = count
    totalCaptured += count
    print(f"Camera {cam} has captured the image of {count} animals.")
    return totalCaptured




#Declaring the size of the simulation area
width = 200
height = 200
locations = np.array([[50, 150], [150, 150], [50, 50], [150, 50]])
print(locations)

animal = np.round(np.random.rand(100,2) * [width, height], 2)
inside_counts = np.zeros(len(locations), dtype=int)
total_count = 0
#To Visualize the grid
detect_radius = 25.0
fig, ax1 = plt.subplots(figsize=(6, 6))  

print(animal)

ax1.set_xlim(0, width)
ax1.set_ylim(0, height)


for i, (x,y) in enumerate(animal):
    ax1.scatter(x, y, color='green', s=50, marker='o', label='Animal' if i == 0 else "")
    ax1.text(x + 2, y + 2, f"A{i+1}", color='green', fontsize=9)


for i, (x, y) in enumerate(locations):
    ax1.scatter(x, y, color='red', marker='>', s=100, label='Camera' if i==0 else "")
    circle = plt.Circle((x, y), detect_radius, color='black', fill=False, alpha=1, linewidth=2)
    ax1.add_patch(circle)
    ax1.text(x+2, y+2, f"C{i}", color='red', fontsize=9)
    total_count = detectAnimal(animal, x, y, detect_radius, i, inside_counts, total_count)   



# Count animals within detection radius of each camera




print(f"Total amount detected is: {total_count}")
print(f"Weighted average for the full area is: {total_count*5}")


plt.show()