import os
import subprocess

def decode_images_to_text(images_dir):
    # Get a list of images in the specified directory
    image_files = [file for file in os.listdir(images_dir) if file.endswith('.jpg')]

    # Sort the image files based on their names
    image_files.sort()

    # Initialize an empty string to store the decoded message
    decoded_message = ""

    # Iterate through the sorted image files
    for image_file in image_files:
        # Get the full path to the image
        image_path = os.path.join(images_dir, image_file)

        # Use exiftool to extract ASCII values from metadata fields
        result = subprocess.run(['exiftool', '-Rating', '-YResolution', '-XResolution', '-ExifVersion', '-n', image_path], capture_output=True)

        # Extract numeric values from the result
        numeric_values = [value for value in result.stdout.decode().split() if value.isdigit()]

        # Convert numeric values to integers and then to characters
        decoded_message += ''.join(chr(int(value)) for value in numeric_values if int(value) != 301)

    print("Decoded Message:", decoded_message)

# Example usage:
images_directory = "dest"
decode_images_to_text(images_directory)
