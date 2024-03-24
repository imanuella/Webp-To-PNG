import glob
import os
from webptools import dwebp  # library to convert webp to png

# Prompt the user to enter the directory path containing webp files
directory_path = input("Enter the directory path containing webp files: ")

# Create an output directory
output_directory = os.path.join(directory_path, "output")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Change the current working directory to the specified directory
os.chdir(directory_path)

# Scans directory for webp files
webp_list = glob.glob("*.webp")

# Using a for loop to go through the files in the list
for filename in webp_list:
    # Print the filename being processed
    print(f"Processing: {filename}")

    # Remove the .webp extension and maintain the original filename for output
    base_filename, _ = os.path.splitext(filename)
    outname = os.path.join(output_directory, f"{base_filename}.png")  # Specify output directory for the converted files
    input_image = f'"{filename}"'  # Wrap the input filename in double quotes
    dwebp(input_image=input_image, output_image=outname, option="-o", logging="-v")

# Print a message after processing all files
print("All files processed successfully!")
