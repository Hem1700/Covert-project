import base64
from exiftool import ExifTool
import os
import glob

def encode_message(message):
    # Encode the message using base64
    encoded_message = base64.b64encode(message.encode()).decode()
    return encoded_message

def hide_message_in_metadata(image_path, encoded_message, image_index, total_images):
    with ExifTool() as et:
        # Hide parts of the encoded message in metadata fields
        et.execute(image_path, ImageDescription=encoded_message)
        et.execute(image_path, Make=f'{image_index}/{total_images}')

def encode_and_send_message(image_directory, message):
    # Encode the message
    encoded_message = encode_message(message)

    # Get the total number of images in the directory
    total_images = len(glob.glob(os.path.join(image_directory, '*.jpg')))

    # Hide the encoded message in metadata fields of each image
    image_files = glob.glob(os.path.join(image_directory, '*.jpg'))
    for i, image_path in enumerate(image_files):
        hide_message_in_metadata(image_path, encoded_message, i + 1, total_images)

    print('Message hidden in metadata fields across', total_images, 'images.')

# Sample message to encrypt
message_to_send = "This is a secret message."

# Sample directory containing images
image_directory_to_send = 'path_to_your_image_directory'  # Replace with the actual directory path

# Encode the message and send it by hiding in image metadata
encode_and_send_message(image_directory_to_send, message_to_send)
