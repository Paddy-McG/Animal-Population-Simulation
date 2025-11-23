import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import csv

def detectAnimal(position, x, y, radius):
    dist = np.sqrt((position[:, 0] - x)**2 + (position[:, 1] - y)**2)
    captured = dist <= radius
    return np.sum(captured)

#Declaring the size of the simulation area 
width = 200
height = 200
total_count = 0
timer = 9
detect_radius = 25.0

locations = np.array([[50, 150], [150, 150], [50, 50], [150, 50]])

animal = np.round(np.random.rand(100,2) * [width, height], 2)
inside_counts = np.zeros(len(locations), dtype=int) 

fig, ax1 = plt.subplots(figsize=(6, 6))  

ax1.set_xlim(0, width)
ax1.set_ylim(0, height)

for i, (x, y) in enumerate(locations):
    ax1.scatter(x, y, color='red', marker='>', s=100, label='Camera' if i==0 else "")
    circle = plt.Circle((x, y), detect_radius, color='black', fill=False, alpha=1, linewidth=2)
    ax1.add_patch(circle)
    ax1.text(x+2, y+2, f"C{i}", color='red', fontsize=9) 

animal_scatter = ax1.scatter(animal[:, 0], animal[:, 1], color='green', s=50)

def update(frame):
    global animal, total_count, inside_counts
    # Random walk: small step in x and y
    step_size = 10
    steps = np.random.uniform(-step_size, step_size, size=animal.shape)
    animal += steps
    animal = np.clip(animal, [0, 0], [width, height])  # Keep within bounds

    # Update scatter plot
    animal_scatter.set_offsets(animal)

    # Reset counts
    inside_counts[:] = 0
    total = 0
   
    # Recalculate detections
    for i, (x, y) in enumerate(locations):
        count = detectAnimal(animal, x, y, detect_radius)
        inside_counts[i] = count
        total += count
        
    total_count +=total

    ax1.set_title(f"Total Detected: {total_count}")

# Animate
ani = FuncAnimation(fig, update, frames=range(0,timer), interval=500, repeat=False)
plt.show()
print(f"The Average number of animals detected was {np.round(total_count/(timer+1), 2)}")
print(f"Weighted average for the full area is: {(total_count/(timer+1))*((width*height)/(4*(math.pi*detect_radius*detect_radius)))}")

data = [
    ["Camera 1", "Camera 2", "Camera 3", "Camera 4"],
    [ 1, 5, 6, 9],
    [ 23, 23, 5, 87]
]

with open(r'C:\Users\patri\OneDrive\CompScience FinalYrProject\data.csv', 'w', newline='') as file_object:
    writer = csv.writer(file_object)
    writer.writerows(data)

