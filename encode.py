import os
import subprocess
import shutil

# Get user input message
user_input = input("Enter a message to encode: ")

# Specify the image file and temporary file
image_file = 'img.jpg'  # Replace with your image file name
temp_image_file = 'temp_image.jpg'

try:
    # Check if there are at least two characters in the user's input
    if len(user_input) < 2:
        raise Exception("Please enter at least two characters for encoding.")

    # Get the ASCII values of the first two characters
    ascii_value_1 = ord(user_input[0])
    ascii_value_2 = ord(user_input[1])
    ascii_value_3 = ord(user_input[2])
    ascii_value_4 = ord(user_input[3])

    # Create a copy of the original image to work with
    shutil.copy(image_file, temp_image_file)

    # Use exiftool to set ASCII values into specific metadata fields
    subprocess.run(['exiftool', '-Rating={}'.format(ascii_value_2), '-YResolution={}'.format(ascii_value_1), '-XResolution={}'.format(ascii_value_3), '-ExifVersion={}'.format(ascii_value_4), temp_image_file])

    # Rename the temp image to the original image file name
    os.rename(temp_image_file, image_file)

    print("Metadata updated with ASCII values.")
except Exception as e:
    print("An error occurred:", e)
