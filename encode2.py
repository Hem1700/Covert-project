import os
import subprocess
import shutil
import random

def encode_text_into_images(message, images_dir, output_dir):
    # Calculate the number of images to use
    length = len(message)
    num_images = int(length/4) + 1 if length % 4 > 0 else int(length/4)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Take the required number of images from the pool
    selected_images = [os.path.join(images_dir, image) for image in os.listdir(images_dir)[:num_images]]

    # Iterate through the message in chunks of 4 characters
    for i in range(0, length, 4):
        text_chunk = message[i:i+4]

        # Iterate through the selected images
        for j, image_path in enumerate(selected_images):
            # Get the ASCII values of the first four characters
            ascii_values = [ord(char) for char in text_chunk]
            
            ascii_values.extend([301] * (4 - len(ascii_values)))


            # Specify the Exif data fields to use
            exif_fields = [
                '-Rating={}'.format(ascii_values[1]),
                '-YResolution={}'.format(ascii_values[0]),
                '-XResolution={}'.format(ascii_values[2]),
                '-ExifVersion={}'.format(ascii_values[3])
            ]

            # Create a copy of the original image to work with
            temp_image_file = os.path.join(output_dir, f"{j + 1}.jpg")
            shutil.copy(image_path, temp_image_file)

            # Use exiftool to set ASCII values into specified metadata fields
            subprocess.run(['exiftool', '-overwrite_original', '-n'] + exif_fields + [temp_image_file])

    print(f"Images saved in {output_dir}")

# Example usage:
user_input = input("Enter the message to encode: ")
images_directory = "source"
output_directory = "dest"

encode_text_into_images(user_input, images_directory, output_directory)
