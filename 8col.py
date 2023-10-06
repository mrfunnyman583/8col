import os
import socket
import platform
import subprocess
import getpass
import shutil
import requests
import paramiko  # For SSH
from passlib.hash import sha256_crypt  # For password hashing

def get_system_info():
    # Get system information
    sys_info = {}
    sys_info['Platform'] = platform.system()
    sys_info['Hostname'] = socket.gethostname()
    sys_info['IP Address'] = socket.gethostbyname(socket.gethostname())
    sys_info['Logged in User'] = getpass.getuser()
    return sys_info

def fetch_external_ip():
    # Fetch external IP address using an API
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        external_ip = data['ip']
        return external_ip
    except Exception as e:
        return str(e)

def list_files(directory):
    # List files in a directory
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        return str(e)

def copy_file(src, dest):
    # Copy a file
    try:
        shutil.copy(src, dest)
        return "File copied successfully."
    except Exception as e:
        return str(e)

def remote_shell(host, username, password, port=22):
    # Function to establish an SSH connection to a remote host
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, port=port, username=username, password=password)

        # Now, you can execute commands on the remote host using ssh_client.exec_command()

        # For example, to run 'ls' command remotely:
        stdin, stdout, stderr = ssh_client.exec_command('ls')
        output = stdout.read().decode()

        # Close the SSH connection when done
        ssh_client.close()
        return output

    except Exception as e:
        return str(e)

def generate_password_hash(password):
    # Function to generate a password hash
    return sha256_crypt.using(salt_size=16).hash(password)

def verify_password(password, hashed_password):
    # Function to verify a password against a hash
    return sha256_crypt.verify(password, hashed_password)

def add_firewall_rule(port, protocol='tcp'):
    # Function to add a firewall rule using 'ufw'
    try:
        subprocess.run(['ufw', 'allow', f'{port}/{protocol}'], check=True)
        return f"Firewall rule added for port {port}/{protocol}"
    except subprocess.CalledProcessError as e:
        return str(e)

def list_firewall_rules():
    # Function to list firewall rules using 'ufw'
    try:
        result = subprocess.run(['ufw', 'status', 'verbose'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def network_scan(target_ip):
    # Function to perform a network scan using 'nmap'
    try:
        result = subprocess.run(['nmap', '-T4', '-F', target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def security_audit():
    # Function to perform system security auditing using 'lynis'
    try:
        result = subprocess.run(['lynis', 'audit', 'system'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def traceroute(target_ip):
    # Function to perform a traceroute
    try:
        result = subprocess.run(['traceroute', target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(target_ip):
    # Function to perform a ping
    try:
        result = subprocess.run(['ping', '-c', '4', target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def main():
    while True:
        print("\n===== 8col - Linux Utility Tool =====")
        print("1. Get System Information")
        print("2. Fetch External IP Address")
        print("3. List Files in Directory")
        print("4. Copy a File")
        print("5. Remote Shell Access")
        print("6. Generate Password Hash")
        print("7. Verify Password")
        print("8. Add Firewall Rule")
        print("9. List Firewall Rules")
        print("10. Network Scan")
        print("11. Security Audit")
        print("12. Traceroute")
        print("13. Ping")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sys_info = get_system_info()
            for key, value in sys_info.items():
                print(f"{key}: {value}")

        elif choice == '2':
            external_ip = fetch_external_ip()
            print(f"External IP Address: {external_ip}")

        elif choice == '3':
            directory = input("Enter the directory path: ")
            files = list_files(directory)
            for file in files:
                print(file)

        elif choice == '4':
            src = input("Enter the source file path: ")
            dest = input("Enter the destination directory path: ")
            result = copy_file(src, dest)
            print(result)

        elif choice == '5':
            remote_host = input("Enter the remote host: ")
            remote_user = input("Enter the remote username: ")
            remote_pass = input("Enter the remote password: ")
            remote_output = remote_shell(remote_host, remote_user, remote_pass)
            print(remote_output)

        elif choice == '6':
            password = input("Enter a password to hash: ")
            hashed_password = generate_password_hash(password)
            print(f"Hashed Password: {hashed_password}")

        elif choice == '7':
            password_to_check = input("Enter a password to check: ")
            stored_hashed_password = input("Enter the stored hashed password: ")
            password_verified = verify_password(password_to_check, stored_hashed_password)
            if password_verified:
                print("Password is verified.")
            else:
                print("Password verification failed.")

        elif choice == '8':
            port = input("Enter the port number: ")
            protocol = input("Enter the protocol (default: tcp): ") or 'tcp'
            result = add_firewall_rule(port, protocol)
            print(result)

        elif choice == '9':
            firewall_rules = list_firewall_rules()
            print(firewall_rules)

        elif choice == '10':
            target_ip = input("Enter the target IP address: ")
            scan_result = network_scan(target_ip)
            print(scan_result)

        elif choice == '11':
            audit_result = security_audit()
            print(audit_result)

        elif choice == '12':
            target_ip = input("Enter the target IP address: ")
            traceroute_result = traceroute(target_ip)
            print(traceroute_result)

        elif choice == '13':
            target_ip = input("Enter the target IP address: ")
            ping_result = ping(target_ip)
            print(ping_result)

        elif choice == '0':
            print("Exiting 8col. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
