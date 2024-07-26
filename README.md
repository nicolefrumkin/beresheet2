# Beresheet2 Visualization in Blender

This project contains a Python script for visualizing the Beresheet2 spaceship in Blender using coordinates from a CSV file.

## Description

This script reads coordinates from a CSV file and uses them to animate the location of the Beresheet2 spaceship object in Blender. Each row in the CSV file represents a frame in the animation, with the x, y, and z coordinates defining the position of the spaceship.

## Demo

<img src="https://github.com/user-attachments/assets/3b00a9d5-03df-4a08-b307-1f3d50d5d7a5" alt="Demo Image" width="500" />


## Requirements

- Blender with Python scripting enabled
  
## Installation

1. Ensure you have Blender installed. You can download it from the [Blender website](https://www.blender.org/download/).
2. Clone this repository or download the script file.

## Usage

1. Open Blender and load the scene.
2. Place the CSV file with the coordinates in the directory.
3. Open the script in Blender's text editor and run it.

### Example CSV File

The CSV file should contain rows of Time, x, y, z, vx, vy, vz, Battery Voltage, and Solar Panel Temp:

Time,x (km),y (km),z (km),vx (km/sec),vy (km/sec),vz (km/sec),Battery Voltage,Solar Panel Temp (°C)
18:40.7,-5251.803201,-4447.783653,-1762.877348,4.61306,-7.824839,-4.473316,32,120
19:40.0,-4968.360831,-4903.018829,-2024.609689,4.93933,-7.526578,-4.35223,32.341471,120
20:40.0,-4663.113734,-5345.395983,-2281.883063,5.228901,-7.218743,-4.22259,34.092239,120
21:40.0,-4341.672489,-5769.244748,-2531.23141,5.47951,-6.909715,-4.088485,33.459715,120
22:40.0,-4006.300783,-6174.619435,-2772.459059,5.693723,-6.60354,-3.952255,31.025438,120
23:40.0,-3659.093428,-6561.790691,-3005.498443,5.874558,-6.303395,-3.815833,29.027471,120

## Script

Here is the full Python script for reference:

```python
import bpy
import csv

# Get the object named "beresheet2"
obj = bpy.context.scene.objects.get("beresheet2")

# Check if the object exists
if obj:
    # Open the CSV file for reading
    with open("path/to/your/spaceship_data.csv", 'r') as file:
        csvreader = csv.reader(file)

        # Initialize the frame counter
        frame_number = 0

        # Iterate over the rows in the CSV file
        for row in csvreader:
            # Extract the x, y, z coordinates from the row
            x = float(row[1])
            y = float(row[2])
            z = float(row[3])

            # Set the object's location
            obj.location = (x, y, z)

            # Insert a keyframe for the object's location at the current frame
            obj.keyframe_insert(data_path="location", frame=frame_number)

            # Increment the frame counter
            frame_number += 1
else:
    print("Object 'beresheet2' not found in the scene.")
```

## Contact

For questions or feedback, please contact [nicolefrumkin@gmail.com](mailto:nicolefrumkin@gmail.com).
