import psutil

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

if __name__ == "__main__":
    top_processes = get_top_processes()

    print("Top RAM-consuming processes:")
    for i, (pid, name, memory_usage) in enumerate(top_processes, start=1):
        print(f"{i}. PID: {pid}, Name: {name}, Memory Usage: {memory_usage / (1024 * 1024):.2f} MB")
