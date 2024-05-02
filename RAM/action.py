import subprocess
import random

def get_processes():
    # Run "processes.py" and return the list of processes
    processes_output = subprocess.getoutput("python3 RAM/processes.py")
    processes_list = processes_output.split('\n')
    return processes_list

def kill_random_process(processes_list):
    # Randomly select a process from the list and kill it
    if processes_list:
        random_process = random.choice(processes_list)
        pid_to_kill = random_process.split()[0]
        subprocess.run(["kill", "-9", pid_to_kill])
        print(f"Randomly killed process with PID {pid_to_kill}")

def manual_intervention():
    # Prompt the user to enter a PID for manual intervention
    user_input = input("Enter the PID of the process to kill : ")
    pid_to_kill = f"{user_input.strip()}"
    subprocess.run(["kill", "-9", pid_to_kill])
    print(f"Manually killed process with PID {pid_to_kill}")

def main():
    try:
        # Prompt the user for the choice
        user_input = input("Options:\n1. AI-based RAM Booster\n2. Manual Intervention\nEnter your choice: ")

        if user_input == "1":
            processes_list = get_processes()
            kill_random_process(processes_list)

        elif user_input == "2":
            manual_intervention()

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
