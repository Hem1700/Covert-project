import subprocess
import json

def print_metadata(image_path):
    try:
        # Run ExifTool to get metadata as JSON
        command = ['exiftool', '-j', image_path]
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Parse the JSON output
        metadata = json.loads(result.stdout)[0]

        # Print metadata
        for tag, value in metadata.items():
            print(f'{tag}: {value}')
    except subprocess.CalledProcessError as e:
        print('Error:', e)

# Specify the image file path for which you want to print metadata
image_path = 'image_path'

# Call the function to print metadata
print_metadata(image_path)
