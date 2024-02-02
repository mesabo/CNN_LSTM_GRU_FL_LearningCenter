import requests

# URL of the file to be downloaded
file_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"

response = requests.get(file_url)

if response.status_code == 200:
    file_path = "./data/airline-passengers.csv"
    with open(file_path, "wb") as file:
        file.write(response.content)
    success_message = "File downloaded successfully. File path: " + file_path
else:
    success_message = "Failed to download the file. Status code: " + str(response.status_code)

success_message

