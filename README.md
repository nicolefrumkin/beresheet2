# Beresheet2 Visualization in Blender

This project contains a Python script for visualizing the Beresheet2 spaceship in Blender using coordinates from a CSV file.

## Description

This script reads coordinates from a CSV file and uses them to animate the location of the Beresheet2 spaceship object in Blender. Each row in the CSV file represents a frame in the animation, with the x, y, and z coordinates defining the position of the spaceship.

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

The CSV file should contain rows of x, y, and z coordinates:

```csv
0.0,0.0,0.0
1.0,1.0,1.0
2.0,2.0,2.0
...
```

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
            x = float(row[0])
            y = float(row[1])
            z = float(row[2])

            # Set the object's location
            obj.location = (x, y, z)

            # Insert a keyframe for the object's location at the current frame
            obj.keyframe_insert(data_path="location", frame=frame_number)

            # Increment the frame counter
            frame_number += 1
else:
    print("Object 'beresheet2' not found in the scene.")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).
