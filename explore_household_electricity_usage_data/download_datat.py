import requests
import zipfile
import os

# URL of the zip file to be downloaded
file_url = "https://archive.ics.uci.edu/static/public/235/individual+household+electric+power+consumption.zip"

# Define the destination directory and file path for the zip file
download_dir = "./data"  # Destination directory
zip_file_path = os.path.join(download_dir, "electric_power_consumption.zip")  # Destination file path

# Check if the file already exists
if os.path.exists(zip_file_path):
    success_message = "File already exists. File path: " + zip_file_path
else:
    # Download the file
    response = requests.get(file_url)
    
    if response.status_code == 200:
        # Create the destination directory if it doesn't exist
        os.makedirs(download_dir, exist_ok=True)
        
        # Save the downloaded zip file
        with open(zip_file_path, "wb") as file:
            file.write(response.content)
        
        success_message = "File downloaded successfully. File path: " + zip_file_path
        
        # Unzip the downloaded file (assuming it's a zip archive)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(download_dir)
            success_message += " and unzipped successfully."
    else:
        success_message = "Failed to download the file. Status code: " + str(response.status_code)

success_message
