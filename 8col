import os
import socket
import platform
import subprocess
import getpass
import shutil
import psutil
import requests

# Function to fetch IP information using ipinfo.io API
def fetch_ip_info(ip_address):
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            ip_info = response.json()
            return ip_info
        else:
            return f"Failed to fetch IP information. Status code: {response.status_code}"
    except Exception as e:
        return str(e)

def fetch_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            ip_info = response.json()
            return ip_info["ip"]
        else:
            return f"Failed to fetch IP address. Status code: {response.status_code}"
    except Exception as e:
        return str(e)

# Rest of the functions and menu options
# ...

if __name__ == "__main__":
    while True:
        print("USB Tool Menu:")
        print("1. Fetch Public IP Address")
        print("2. Fetch IP Information")
        print("3. Get System Information")
        print("4. Execute Custom Command")
        print("5. List Files in a Directory")
        print("6. Change Directory")
        print("7. Create Directory")
        print("8. Get Logged-In User")
        print("9. Copy File")
        print("10. Delete File")
        print("11. List Running Processes")
        print("12. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12): ")

        if choice == "1":
            public_ip = fetch_ip_address()
            if not isinstance(public_ip, str):
                print(f"Public IP Address: {public_ip}")
            else:
                print(public_ip)
        elif choice == "2":
            ip_to_lookup = input("Enter the IP address to fetch information: ")
            ip_info = fetch_ip_info(ip_to_lookup)
            if not isinstance(ip_info, str):
                print("IP Information:")
                for key, value in ip_info.items():
                    print(f"{key}: {value}")
            else:
                print(ip_info)
        elif choice == "3":
            system_info = get_system_info()
            for key, value in system_info.items():
                print(f"{key}: {value}")
        elif choice == "4":
            custom_command = input("Enter the custom command: ")
            command_result = execute_command(custom_command)
            print("Command Output:")
            print(command_result)
        elif choice == "5":
            directory_path = input("Enter the directory path: ")
            files = list_files_in_directory(directory_path)
            if isinstance(files, list):
                print("Files in the directory:")
                for file in files:
                    print(file)
            else:
                print(f"Error: {files}")
        elif choice == "6":
            new_directory = input("Enter the new directory path: ")
            directory_change_result = change_directory(new_directory)
            print(directory_change_result)
        elif choice == "7":
            new_directory_name = input("Enter the name of the new directory: ")
            directory_create_result = create_directory(new_directory_name)
            print(directory_create_result)
        elif choice == "8":
            logged_in_user = get_logged_in_user()
            print(f"Logged-In User: {logged_in_user}")
        elif choice == "9":
            source_path = input("Enter the source file path: ")
            destination_path = input("Enter the destination file path: ")
            copy_result = copy_file(source_path, destination_path)
            print(copy_result)
        elif choice == "10":
            file_to_delete = input("Enter the file path to delete: ")
            delete_result = delete_file(file_to_delete)
            print(delete_result)
        elif choice == "11":
            processes = list_running_processes()
            print("Running Processes:")
            for process in processes:
                print(f"PID: {process['PID']}, Name: {process['Name']}, Username: {process['Username']}")
        elif choice == "12":
            print("Exiting USB Tool.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
