import os
import platform
import subprocess
import psutil

# ANSI escape codes for colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def get_hardware_health():
    cpu_info = subprocess.check_output("lscpu", shell=True).decode()
    return cpu_info

def get_os_health():
    os_info = platform.platform()
    return os_info

def get_network_health():
    ping_result = subprocess.run(["ping", "-c", "4", "google.com"], stdout=subprocess.PIPE)
    return ping_result.stdout.decode()

def get_application_health():
    process_list = subprocess.check_output("ps aux", shell=True).decode()
    return process_list

def get_resource_utilization():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    return f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory_usage}%"

def get_compliance_checks():
    process_running = "apache2" in subprocess.check_output("ps aux", shell=True).decode()
    return f"Is Apache running? {'Yes' if process_running else 'No'}"

def get_system_updates():
    update_info = subprocess.check_output("apt list --upgradable", shell=True).decode()
    return update_info


if __name__ == "__main__":
    print("Select the health checks you want to perform:")
    print("1. Hardware Health")
    print("2. Operating System Health")
    print("3. Network Health")
    print("4. Application Health")
    print("5. Resource Utilization")
    print("6. Compliance Checks")
    print("7. System Updates")

    selected_checks = input("Enter the numbers separated by commas (e.g., 1, 3, 5): ").split(',')

    for check in selected_checks:
        check = check.strip()
        if check == '1':
            print(get_hardware_health())
        elif check == '2':
            print(get_os_health())
        elif check == '3':
            print(get_network_health())
        elif check == '4':
            print(get_application_health())
        elif check == '5':
            print(get_resource_utilization())
        elif check == '6':
            print(get_compliance_checks())
        elif check == '7':
            print(get_system_updates())
        else:
            print(f"Invalid option: {check}")
