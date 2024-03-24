import glob
import os
import shutil
from webptools import dwebp  # library to convert webp to png

def convert_webp_to_png(directory):
    # Initialize file count
    total_files = 0
    # List to store paths of converted files
    converted_files = []
    # Scan directory and subdirectories for webp files
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".webp"):
                total_files += 1
                filepath = os.path.join(root, filename)

                # Print the filename being processed
                print(f"Processing: {filepath}")

                # Remove the .webp extension and maintain the original filename for output
                base_filename, _ = os.path.splitext(filename)
                outname = os.path.join(root, f"{base_filename}.png")

                # Wrap the filenames in double quotes to handle paths with spaces
                input_image = f'"{filepath}"'
                output_image = f'"{outname}"'

                # Convert webp to png
                dwebp(input_image=input_image, output_image=output_image, option="-o", logging="-v")

                # Add path of converted file to the list
                converted_files.append(outname)

    return total_files, converted_files

def main():
    # Ask user to input the directory filepath
    directory_path = input("Enter the directory filepath: ").strip('"')

    # Convert webp files to png in the specified directory and its subdirectories
    total_files, converted_files = convert_webp_to_png(directory_path)

    # Create a subdirectory within the input directory for converted files
    output_folder = os.path.join(directory_path, "converted_files")
    os.makedirs(output_folder, exist_ok=True)

    # Move converted files to the output folder
    for file_path in converted_files:
        shutil.move(file_path, output_folder)

    # Print total files converted
    print(f"All {total_files} files processed successfully!")

    # Prompt user to press Enter to exit
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
