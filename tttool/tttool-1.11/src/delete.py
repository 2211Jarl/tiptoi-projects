import os
import shutil

# Path to the directory containing the files
directory = r"D:\ChilliGinger\Tiptoi-experiments\tiptoi-projects\tttool\tttool-1.11\elect-media"  # Change this to your target directory if needed
destination_directory = os.path.join(directory, "moved_files")

if not os.path.exists(destination_directory): os.makedirs(destination_directory)

# Loop through even numbers from 8 to 108
for i in range(8, 109, 2):  # 109 is exclusive, so it includes 108
    filename = f"elect_{i:02d}.ogg"  # Zero-padded two-digit number (e.g., file_08)
    filepath = os.path.join(directory, filename)
    dest = os.path.join(destination_directory, filename)

    # Delete the file if it exists
    if os.path.isfile(filepath):
        shutil.move(filepath, dest)
        print(f"Moved: {filename}")
    else:
        print(f"File not found: {filename}")
