import psutil

def list_processes():
    # Get a list of all running processes
    all_processes = psutil.process_iter()

    # Print header
    print("{:<8} {:<20} {:<10}".format("PID", "Name", "Status"))
    print("="*40)

    for process in all_processes:
        try:
            # Get process details
            process_info = process.as_dict(attrs=['pid', 'name', 'status'])
            
            if process_info['status'] == 'running':
                # Print process details
                print("{:<8} {:<20} {:<10}".format(
                    process_info['pid'], process_info['name'], process_info['status']
                ))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle exceptions that may occur during process retrieval
            pass

if __name__ == "__main__":
    list_processes()
