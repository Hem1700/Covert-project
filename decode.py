import os
import subprocess

def decode_messages_from_images(encoded_image_dir):
    decoded_messages = []

    try:
        # Get a list of image files in the encoded image directory
        image_files = sorted(os.listdir(encoded_image_dir))

        for image_file in image_files:
            if not image_file.endswith('.jpg'):
                continue

            # Use exiftool to extract ASCII values from metadata
            exiftool_commands = [
                '-Rating',
                '-YResolution',
                '-XResolution',
                '-ExifVersion'
            ]

            exiftool_output = subprocess.check_output(['exiftool'] + exiftool_commands + [os.path.join(encoded_image_dir, image_file)]).decode()

            # Extract ASCII values from the exiftool output
            ascii_values = [int(value) for value in exiftool_output.split('\n') if value]

            # Convert ASCII values to characters and add to the decoded message
            decoded_message = ''.join(chr(ascii) for ascii in ascii_values)
            decoded_messages.append(decoded_message)

        return decoded_messages
    except Exception as e:
        return str(e)

# Specify the directory containing encoded images
encoded_image_directory = 'encoded_images'  # Change to the directory containing your encoded images

# Call the decoding function
decoded_messages = decode_messages_from_images(encoded_image_directory)

# Print the decoded messages
for i, message in enumerate(decoded_messages):
    print(f"Decoded message {i + 1}: {message}")
