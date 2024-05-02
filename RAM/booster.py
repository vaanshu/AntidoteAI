import psutil
import os
import random

def get_top_processes(n=5):
    processes = []

    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            process_info = process.info
            processes.append((process_info['pid'], process_info['name'], process_info['memory_info'].rss))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    processes.sort(key=lambda x: x[2], reverse=True)
    return processes[:n]

def ai_decision():
    # Replace this with a more sophisticated AI decision-making process
    return random.choice(["boost", "skip"])

def manual_decision():
    try:
        choice = int(input("Enter the number of the process to manually terminate (0 to skip): "))
        return choice
    except ValueError:
        return 0

def list_and_boost_processes():
    top_processes = get_top_processes()

    print("Top RAM-consuming processes:")
    for i, (pid, name, memory_usage) in enumerate(top_processes, start=1):
        print(f"{i}. PID: {pid}, Name: {name}, Memory Usage: {memory_usage / (1024 * 1024):.2f} MB")

    try:
        ai_action = ai_decision()

        print("\nOptions:")
        print("1. AI-based RAM Booster")
        print("2. Manual Intervention")

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1 and ai_action == "boost":
            print("AI-based RAM Booster activated.")
            # Implement AI-based RAM boosting logic here
        elif user_choice == 2:
            manual_action = manual_decision()
            if manual_action != 0 and 0 < manual_action <= len(top_processes):
                pid_to_kill = top_processes[manual_action - 1][0]
                os.system(f"kill -9 {pid_to_kill}")
                print(f"Process with PID {pid_to_kill} manually terminated successfully.")
            else:
                print("Invalid choice or skipping action.")
        else:
            print("Skipping action.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_and_boost_processes()
