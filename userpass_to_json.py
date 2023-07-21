import json
import os

# Function to convert a single username:password string to a dictionary
def parse_username_password(pair):
    username, password = pair.split(':')
    return {"username": username, "password": password}

# Function to read data from the text file and convert it to JSON
def convert_to_json(file_path):
    with open(file_path, 'r') as file:
        usernames_passwords = [line.strip() for line in file]
    accounts = [parse_username_password(pair) for pair in usernames_passwords]
    data = {
        "accounts": accounts,
        "server_url": "wss://placede.ml"
    }
    return json.dumps(data, indent=4)

# Provide the file path here
file_path = "path/to/file.txt"

# Get the current directory where the script is run from
current_directory = os.path.dirname(os.path.abspath(__file__))

# Convert the data to JSON
json_string = convert_to_json(file_path)

# Save the JSON string to config.json in the current directory
output_file_path = os.path.join(current_directory, "config.json")
with open(output_file_path, 'w') as output_file:
    output_file.write(json_string)

print("Conversion completed. JSON data saved to config.json.")