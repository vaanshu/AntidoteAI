import psutil
import os

def check_running_processes():
    for process in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            process_info = process.info
            pid = process_info['pid']
            name = process_info['name']
            exe = process_info['exe']

            print(f"Checking process: PID {pid}, Name {name}, Executable {exe}",end="")

            # Check if the file is an executable
            if exe is not None and os.path.isfile(exe):
                try:
                    analysis_result = os.system("python3 PE/extractPE.py {}".format(exe))
                    print(f"Analysis result: {analysis_result}")
                    # You can take further actions based on the analysis result
                except Exception as e:
                    print(f"Error analyzing file: {e}")
            else:
                print("-------------------------------Skipping non-executable or unknown executable.")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print("Error accessing process information.")

if __name__ == "__main__":
    check_running_processes()
