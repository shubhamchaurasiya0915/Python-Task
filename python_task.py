import subprocess
import pyautogui
import platform
import os
import psutil
import GPUtil
import psutil
import tkinter as tk
# import uuid
import requests
import platform


def get_installed_software():
    try:
        # Run the wmic command to get the list of installed software
        result = subprocess.run(['wmic', 'product', 'get', 'name'], capture_output=True, text=True, check=True)

        # Extract the installed software names from the command output
        installed_software = result.stdout.strip().split('\n')[1:]

        # Print the list of installed software
        print("List of Installed Software:")
        for software in installed_software:
            print(software.strip())

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to retrieve the list of installed software.")

if __name__ == "__main__":
    get_installed_software()

# 3
def get_screen_resolution():
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    print(f"Screen Resolution: {screen_width} x {screen_height} pixels")

if __name__ == "__main__":
    get_screen_resolution()

# 4
def get_cpu_model():
    # Get the CPU model information
    cpu_model = platform.processor()

    print(f"CPU Model: {cpu_model}")

if __name__ == "__main__":
    get_cpu_model()

# 5
def get_cpu_info():
    # Get the number of CPU cores
    cpu_cores = os.cpu_count()

    # Get the number of CPU threads
    cpu_threads = psutil.cpu_count(logical=True)

    print(f"Number of CPU Cores: {cpu_cores}")
    print(f"Number of CPU Threads: {cpu_threads}")

if __name__ == "__main__":
    get_cpu_info()

# 6

def get_gpu_model():
    try:
        # Get the list of available GPUs
        gpus = GPUtil.getGPUs()

        if gpus:
            # Assuming you are interested in the model of the first GPU
            gpu_model = gpus[0].name
            print(f"GPU Model: {gpu_model}")
        else:
            print("No GPU detected on this system.")

    except Exception as e:
        print(f"Error: {e}")
        print("Failed to retrieve GPU information.")

if __name__ == "__main__":
    get_gpu_model()

# 7

def get_ram_size():
    # Get the total RAM size in bytes
    ram_bytes = psutil.virtual_memory().total

    # Convert bytes to gigabytes
    ram_gb = ram_bytes / (1024**3)

    print(f"RAM Size: {ram_gb:.2f} GB")

if __name__ == "__main__":
    get_ram_size()

# 8


def get_screen_size():
    root = tk.Tk()
    root.update_idletasks()  # Ensure window attributes are up-to-date
    width_mm = root.winfo_screenmmwidth()
    height_mm = root.winfo_screenmmheight()
    root.destroy()

    # Convert from millimeters to inches (1 inch = 25.4 mm)
    width_inches = width_mm / 25.4
    height_inches = height_mm / 25.4

    print(f"Screen Size: {width_inches:.2f} inches x {height_inches:.2f} inches")

if __name__ == "__main__":
    get_screen_size()

# 9

from getmac import get_mac_address

def get_mac_addresses():
    try:
       
        wifi_mac = get_mac_address(interface="Wi-Fi")
        print(f"Wi-Fi MAC Address: {wifi_mac}")

        
        ethernet_mac = get_mac_address(interface="Ethernet")
        print(f"Ethernet MAC Address: {ethernet_mac}")

    except Exception as e:
        print(f"Error: {e}")
        print("Failed to retrieve MAC addresses.")

if __name__ == "__main__":
    get_mac_addresses()

# 10


def get_public_ip():
    try:
        # Make a request to httpbin.org to get your public IP address
        response = requests.get("https://httpbin.org/ip")

        # Parse the JSON response to get the public IP address
        public_ip = response.json()["origin"]
        
        print(f"Public IP Address: {public_ip}")

    except Exception as e:
        print(f"Error: {e}")
        print("Failed to retrieve public IP address.")

if __name__ == "__main__":
    get_public_ip()

# 11

def get_windows_version():
    try:
        # Get the Windows version information
        windows_version = platform.version()

        print(f"Windows Version: {windows_version}")

    except Exception as e:
        print(f"Error: {e}")
        print("Failed to retrieve Windows version information.")

if __name__ == "__main__":
    get_windows_version()
