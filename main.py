import glob
import os
import shutil
from webptools import dwebp

def convert_webp_to_png(directory):
    total_files = 0
    converted_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".webp"):
                total_files += 1
                filepath = os.path.join(root, filename)
                print(f"Processing: {filepath}")

                base_filename, _ = os.path.splitext(filename)
                outname = os.path.join(root, f"{base_filename}.png")

                input_image = f'"{filepath}"'
                output_image = f'"{outname}"'
                dwebp(input_image=input_image, output_image=output_image, option="-o", logging="-v")
                converted_files.append(outname)

    return total_files, converted_files

def main():
    directory_path = input("Enter the directory filepath: ").strip('"')
    total_files, converted_files = convert_webp_to_png(directory_path)

    output_folder = os.path.join(directory_path, "converted_files")
    os.makedirs(output_folder, exist_ok=True)
    for file_path in converted_files:
        shutil.move(file_path, output_folder)

    print(f"All {total_files} files processed successfully!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
