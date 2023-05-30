import datetime
import platform

current_datetime = datetime.datetime.now()
os_name = platform.system()
os_version = platform.release()


# Create the content to write to the file
content = f"Current Datetime: {current_datetime}\nOS Name: {os_name}, OS Version: {os_version}"

# Specify the file path
file_path = "output.txt"

# Open the file
with open(file_path, "w") as file:
    # Write the content to the file
    file.write(content)

print(f"Data written to {file_path} successfully.")
