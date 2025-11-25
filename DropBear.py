import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import csv
import os
os.environ["OMP_NUM_THREADS"] = "1"
from sklearn.cluster import KMeans

def detectAnimal(position, x, y, radius):
    dist = np.sqrt((position[:, 0] - x)**2 + (position[:, 1] - y)**2)
    captured = dist <= radius
    return np.sum(captured)

def distance(x1, x2):
    return np.sqrt(np.power(x1-x2, 2))

def updateCenter(animal):
     Centers = [[animal[0,0], animal[0,1]],
                [animal[1,0], animal[1,1]],
                [animal[2,0], animal[2,1]],
                [animal[3,0], animal[3,1]]]
     return Centers

#Declaring the size of the simulation area 
width = 200
height = 200
total_count = 0
timer = 29
detect_radius = 25.0

animal = np.round(np.random.rand(100,2) * [width, height], 2)

#Declaring the amount of clusters and what movement we want (Random/Cluster)
k = 4  
movement = "Cluster"
centers = updateCenter(animal)

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
cluster_scatter = ax1.scatter([], [], color='blue', marker='x', s=100, label='Cluster Center')

# Creating The csv file that we willl send the data to 
data = ["Camera 1", "Camera 2", "Camera 3", "Camera 4"]
with open(r'C:\Users\patri\OneDrive\CompScience FinalYrProject\data.csv', 'w', newline='') as file_object:
    writer = csv.writer(file_object)
    writer.writerow(data)



def update(frame):
    global animal, total_count, inside_counts, centers


    if(movement == "Random"):

        # Random walk: small step in x and y
        step_size = 10
        steps = np.random.uniform(-step_size, step_size, size=animal.shape)
        animal += steps
        animal = np.clip(animal, [0, 0], [width, height])  # Keep within bounds

    elif(movement == "Cluster"):

        step_size = 5
        kmeans = KMeans(n_clusters=k, n_init=10)
        kmeans.fit(animal)
        labels = kmeans.labels_
        
        # error detection    print(centers)

        # Move each animal toward its cluster center
        for i in range(len(animal)):
            center = centers[labels[i]]
            direction = center - animal[i]
            norm = np.linalg.norm(direction)
            if norm > 0:
                direction = (direction / norm) * step_size
            # Add a little randomness so they don’t overlap perfectly
            jitter = np.random.uniform(-1, 1, size=2)
            animal[i] += direction + 0.3 * jitter

        centers = updateCenter(animal)
        # Keep animals inside bounds
        animal = np.clip(animal, [0, 0], [width, height])

        cluster_scatter.set_offsets(centers)

        # Color animals by cluster
        animal_scatter.set_color([plt.cm.tab10(label) for label in labels])



    
    
    # Update scatter plot
    animal_scatter.set_offsets(animal)


    # Reset counts before starting the detection
    inside_counts[:] = 0
    total = 0

    # Recalculate detections
    for i, (x, y) in enumerate(locations):
        count = detectAnimal(animal, x, y, detect_radius)
        inside_counts[i] = count
        total += count


    total_count += total
    ax1.set_title(f"Total Detected: {total_count}")

    # --- KMeans clustering ---
    #kmeans = KMeans(n_clusters=k, n_init=10)
    #kmeans.fit(animal)
    #labels = kmeans.labels_
    #centers = kmeans.cluster_centers_

    # Color animals by cluster
    #animal_scatter.set_color([plt.cm.tab10(label) for label in labels])

    # Update cluster centers
    #cluster_scatter.set_offsets(centers)


    #---------- Writing the detection numbers to a csv file we created above ------------#
    saw = [inside_counts[0], inside_counts[1], inside_counts[2], inside_counts[3]]
    with open(r'C:\Users\patri\OneDrive\CompScience FinalYrProject\data.csv', 'a', newline='') as file_object:
        writer = csv.writer(file_object)
        writer.writerow(saw)

        

# Animate
ani = FuncAnimation(fig, update, frames=range(0,timer), interval=500, repeat=False)
plt.show()
print(f"The Average number of animals detected was {np.round(total_count/(timer+1), 2)}")
print(f"Weighted average for the full area is: {(total_count/(timer+1))*((width*height)/(4*(math.pi*detect_radius*detect_radius)))}")