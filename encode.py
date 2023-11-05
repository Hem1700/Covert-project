import os
import subprocess
import shutil

def encode_message_in_images(input_image_dir, message, output_image_dir):
    try:
        # Check if the message is not empty
        if not message:
            raise ValueError("Please enter a message for encoding.")

        # Split the message into segments of 4 characters each
        segments = [message[i:i+4] for i in range(0, len(message), 4)]

        # Create the output directory if it doesn't exist
        os.makedirs(output_image_dir, exist_ok=True)

        image_files = sorted(os.listdir(input_image_dir))

        for i, segment in enumerate(segments):
            if i >= len(image_files):
                raise ValueError("Not enough input images to encode the message.")

            input_image_path = os.path.join(input_image_dir, image_files[i])
            output_image_path = os.path.join(output_image_dir, f'encoded_image_{i}.jpg')

            # Get the ASCII values of the characters in the segment
            ascii_values = [ord(char) for char in segment]

            # Create a copy of the input image to work with
            shutil.copy(input_image_path, output_image_path)

            # Use exiftool to set ASCII values into specific metadata fields
            exiftool_commands = [
                '-Rating={}'.format(ascii_values[1]),
                '-YResolution={}'.format(ascii_values[0]),
                '-XResolution={}'.format(ascii_values[2]),
                '-ExifVersion={}'.format(ascii_values[3])
            ]

            subprocess.run(['exiftool'] + exiftool_commands + [output_image_path])

            print("Metadata updated with ASCII values for segment {}: {}".format(i, segment))

        print("Message encoded successfully. Encoded images saved in directory:", output_image_dir)
    except Exception as e:
        print("An error occurred:", e)

# Get user input message
user_input = input("Enter a message to encode: ")

# Specify the directory containing input images
input_image_directory = 'input_images'  # Replace with the directory containing your input images

# Specify the directory for saving encoded images
output_image_directory = 'encoded_images'  # Change to your preferred directory name

# Call the encoding function
encode_message_in_images(input_image_directory, user_input, output_image_directory)
