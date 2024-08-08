import glob
import os
from webptools import dwebp  


directory_path = input("Enter the directory path containing webp files: ")
output_directory = os.path.join(directory_path, "output")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
os.chdir(directory_path)

webp_list = glob.glob("*.webp")
for filename in webp_list:
    print(f"Processing: {filename}")

    base_filename, _ = os.path.splitext(filename)
    outname = os.path.join(output_directory, f"{base_filename}.png")  
    input_image = f'"{filename}"' 
    dwebp(input_image=input_image, output_image=outname, option="-o", logging="-v")
    
print("All files processed successfully!")
