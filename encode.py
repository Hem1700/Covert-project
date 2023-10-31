import os
import subprocess
import shutil

def encode_message_in_image(image_file, user_input):
    try:
        if len(user_input) < 4:
            raise ValueError("Please enter at least four characters for encoding.")

        # Get the ASCII values of the first four characters
        ascii_values = [ord(char) for char in user_input[:4]]

        # Create a copy of the original image to work with
        temp_image_file = 'temp_image.jpg'
        shutil.copy(image_file, temp_image_file)

        # Use exiftool to set ASCII values into specific metadata fields
        exiftool_commands = [
            '-Rating={}'.format(ascii_values[1]),
            '-YResolution={}'.format(ascii_values[0]),
            '-XResolution={}'.format(ascii_values[2]),
            '-ExifVersion={}'.format(ascii_values[3])
        ]

        subprocess.run(['exiftool'] + exiftool_commands + [temp_image_file])

        # Rename the temp image to the original image file name
        os.rename(temp_image_file, image_file)

        print("Metadata updated with ASCII values.")
    except Exception as e:
        print("An error occurred:", e)

# Get user input message
user_input = input("Enter a message to encode: ")

# Specify the image file
image_file = 'img.jpg'  # Replace with your image file name

# Call the encoding function
encode_message_in_image(image_file, user_input)
