import os
import subprocess
import shutil

def encode_message_in_images(base_image, message, output_directory):
    try:
        # Check if the message is not empty
        if not message:
            raise ValueError("Please enter a message for encoding.")

        # Split the message into segments of 4 characters each
        segments = [message[i:i+4] for i in range(0, len(message), 4)]

        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        for i, segment in enumerate(segments):
            # Create a copy of the base image to work with
            temp_image = os.path.join(output_directory, f'image_{i}.jpg')
            shutil.copy(base_image, temp_image)

            # Get the ASCII values of the characters in the segment
            ascii_values = [ord(char) for char in segment]

            # Use exiftool to set ASCII values into specific metadata fields
            exiftool_commands = [
                '-Rating={}'.format(ascii_values[1]),
                '-YResolution={}'.format(ascii_values[0]),
                '-XResolution={}'.format(ascii_values[2]),
                '-ExifVersion={}'.format(ascii_values[3])
            ]

            subprocess.run(['exiftool'] + exiftool_commands + [temp_image])

            print("Metadata updated with ASCII values for segment {}: {}".format(i, segment))

        print("Message encoded successfully. Images stored in directory:", output_directory)
    except Exception as e:
        print("An error occurred:", e)

# Get user input message
user_input = input("Enter a message to encode: ")

# Specify the base image file
base_image_file = 'img.jpg'  # Replace with your base image file name

# Specify the output directory for storing encoded images
output_directory = 'encoded_images'  # You can change this to your preferred directory name

# Call the encoding function
encode_message_in_images(base_image_file, user_input, output_directory)
