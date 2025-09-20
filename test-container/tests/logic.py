
### testing for svg
import os
import glob

directory_path = "../amino-guesser/assets/svg"  # Replace with your directory path

# Get all files (e.g., all files ending with .txt)
txt_files = glob.glob(os.path.join(directory_path, "*.svg"))


for svg in txt_files:
    print(os.path.basename(svg)) # Prints just the filename

