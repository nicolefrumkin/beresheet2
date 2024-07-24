import bpy
import csv

# Get the object named "beresheet2"
obj = bpy.context.scene.objects.get("beresheet2")

# Check if the object exists
if obj:
    # Open the CSV file for reading
    with open(".../spaceship_data.csv", 'r') as file:
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
