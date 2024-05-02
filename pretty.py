import tkinter as tk
from tkinter import ttk, simpledialog, scrolledtext
import os
import subprocess
import random
from collections import defaultdict
import platform
import psutil
import hashlib

class AntidoteAIApp:

    def __init__(self, root):
        self.root = root
        root.title("Antidote - AI based Antivirus")
        root.configure(background="lightgrey")

        self.style = ttk.Style()
        self.style.configure("Red.TButton", foreground="white", background="green")
        self.style.map("Red.TButton", background=[("active", "black")])

        self.style.configure("Green.TFrame", background="white")

        button_frame = ttk.Frame(root, padding="10", style="Green.TFrame")
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        pe_button = ttk.Button(button_frame, text="PE Scanner", command=lambda: self.run_command(self.run_PE),
                               style="Red.TButton", padding=(5, 5))
        pe_button.pack(pady=5, fill=tk.X, expand=True)
        pe_button.bind("<Enter>", self.set_hand_cursor)
        pe_button.bind("<Leave>", lambda e: root.config(cursor=""))

        url_button = ttk.Button(button_frame, text="URL Scanner", command=lambda: self.run_command(self.run_URL),
                                style="Red.TButton", padding=(5, 5))
        url_button.pack(pady=5, fill=tk.X, expand=True)
        url_button.bind("<Enter>", self.set_hand_cursor)
        url_button.bind("<Leave>", lambda e: root.config(cursor=""))

        ram_button = ttk.Button(button_frame, text="RAM Booster", command=self.run_RamBooster,
                                style="Red.TButton", padding=(5, 5))
        ram_button.pack(pady=5, fill=tk.X, expand=True)
        ram_button.bind("<Enter>", self.set_hand_cursor)
        ram_button.bind("<Leave>", lambda e: root.config(cursor=""))

        junk_button = ttk.Button(button_frame, text="Junk File Finder", command=lambda: self.run_command(self.run_JunkFileRemover),
                                 style="Red.TButton", padding=(5, 5))
        junk_button.pack(pady=5, fill=tk.X, expand=True)
        junk_button.bind("<Enter>", self.set_hand_cursor)
        junk_button.bind("<Leave>", lambda e: root.config(cursor=""))

        '''exe_button = ttk.Button(button_frame, text="Running processes", command=lambda: self.run_command(self.run_BGexeLiveScanner),
                                style="Red.TButton", padding=(5, 5))
        exe_button.pack(pady=5, fill=tk.X, expand=True)
        exe_button.bind("<Enter>", self.set_hand_cursor)
        exe_button.bind("<Leave>", lambda e: root.config(cursor=""))'''

        health_button = ttk.Button(button_frame, text="System Health Checker", command=lambda: self.run_command(self.run_systemHealthchecker),
                                   style="Red.TButton", padding=(5, 5))
        health_button.pack(pady=5, fill=tk.X, expand=True)
        health_button.bind("<Enter>", self.set_hand_cursor)
        health_button.bind("<Leave>", lambda e: root.config(cursor=""))

        output_frame = ttk.Frame(root, padding="10")
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        output_frame.bind("<Enter>", self.set_x_cursor)
        output_frame.bind("<Leave>", lambda e: root.config(cursor=""))

        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=60, height=15, bg="white", fg="black")
        self.output_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def set_hand_cursor(self, event):
        self.root.config(cursor="hand2")

    def set_x_cursor(self, event):
        self.root.config(cursor="X_cursor")

    def exit_program(self):
        exit()

    def append_output(self, text):
        self.output_text.delete(1.0, tk.END)
        lines = text.split('\n')
        for line in lines:
            self.output_text.insert(tk.END, line + '\n')

    def run_command(self, command_func):
        output = os.popen(command_func()).read()
        self.append_output(output)

    def run_PE(self):
        file = simpledialog.askstring("PE Scanner", "Enter the path and name of the file:")
        return "python3 newpe/extractPE.py {}".format(file)

    def run_URL(self):
        url = simpledialog.askstring("URL Scanner", "Enter the URL:")
        return "python3 URL/extractURL.py {}".format(url)

    def run_RamBooster(self):
        try:
            processes_output = subprocess.getoutput("python3 RAM/processes.py")
            self.append_output("Processes:\n" + processes_output)

            ram_booster_dialog = tk.Toplevel(self.root)
            ram_booster_dialog.title("RAM Booster Options")

            def on_button_click(option):
                ram_booster_dialog.destroy()
                self.handle_ram_booster_option(option)

            ai_button = ttk.Button(ram_booster_dialog, text="AI-based RAM Booster", command=lambda: on_button_click(1))
            ai_button.pack(pady=5, fill=tk.X, expand=True)

            manual_button = ttk.Button(ram_booster_dialog, text="Manual Intervention", command=lambda: on_button_click(2))
            manual_button.pack(pady=5, fill=tk.X, expand=True)

        except Exception as e:
            self.append_output(f"An error occurred: {str(e)}")

    def handle_ram_booster_option(self, option):
        try:
            if option == 1:
                processes_list = subprocess.getoutput("python3 RAM/processes.py").split('\n')
                if processes_list:
                    random_process = random.choice(processes_list)
                    pid_to_kill = random_process.split()[0]
                    subprocess.run(["kill", "-9", pid_to_kill])
                    self.append_output(f"Randomly killed process with PID {pid_to_kill}")
                else:
                    self.append_output("No processes available for AI-based RAM Booster.")

            elif option == 2:
                manual_input = tk.simpledialog.askstring("Manual Intervention", "Enter manual input (process PID to terminate):")
                pid_to_kill = f"{manual_input.strip()}"
                subprocess.run(["kill", "-9", pid_to_kill])
                self.append_output(f"Manually killed process with PID {pid_to_kill}")

            else:
                self.append_output("Invalid choice. Please enter 1 or 2.")

        except Exception as e:
            self.append_output(f"An error occurred: {str(e)}")

    def run_JunkFileRemover(self):
        def find_duplicate_files(directory):
            file_hash_dict = defaultdict(list)

            for foldername, subfolders, filenames in os.walk(directory):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)

                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()

                    file_hash_dict[file_hash].append(file_path)

            duplicate_files = [files for files in file_hash_dict.values() if len(files) > 1]

            if duplicate_files:
                return duplicate_files
            else:
                return ["NO DUPLICATE FILES FOUND"]

        def find_junk_files(directory):
            junk_extensions = ['.tmp', '.bak', '.log', '.swp']

            deleted_files = []

            for foldername, subfolders, filenames in os.walk(directory):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    _, file_extension = os.path.splitext(filename)

                    if file_extension in junk_extensions:
                        try:
                            os.remove(file_path)
                            deleted_files.append(file_path)
                        except Exception as e:
                            print(f"Error deleting {file_path}: {e}")

            if deleted_files:
                return deleted_files
            else:
                return ["NO JUNK FILES"]

        target_directory = simpledialog.askstring("Input", "Enter target directory path for search:")

        if target_directory:
            choice = simpledialog.askinteger("Input", "Enter Choice:\n1. Check for Duplicate Files\n2. Check for Junk Files", minvalue=1, maxvalue=2)

            if choice == 1:
                duplicate_files = find_duplicate_files(target_directory)
                self.append_output(" duplicate files : ")
                self.append_output('\n\n'.join(['\n'.join(files) for files in duplicate_files]))
            elif choice == 2:
                self.append_output(" junk files : ")
                junk_files = find_junk_files(target_directory)
                self.append_output('\n'.join(junk_files))

    def run_BGexeLiveScanner(self):
        return "python3 LIVEexe/x.py"

    def run_systemHealthchecker(self):
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

        results = []
        check = simpledialog.askinteger("Input", "Enter Choice:\n1. Hardware Health\n2. OS Health\n3. Network Health\n4. Application Health\n5. Resource Health\n6. Compliance Health\n7. System Updates", minvalue=1, maxvalue=7)

        if check == 1:
            results.append(get_hardware_health())
        elif check == 2:
            results.append(get_os_health())
        elif check == 3:
            results.append(get_network_health())
        elif check == 4:
            results.append(get_application_health())
        elif check == 5:
            results.append(get_resource_utilization())
        elif check == 6:
            results.append(get_compliance_checks())
        elif check == 7:
            results.append(get_system_updates())
        else:
            results.append(f"Invalid option: {check}")

        self.append_output('\n'.join(results))

    def run(self):
        self.root.destroy()
        new_root = tk.Tk()
        app = AntidoteAIApp(new_root)
        new_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AntidoteAIApp(root)
    root.mainloop()
