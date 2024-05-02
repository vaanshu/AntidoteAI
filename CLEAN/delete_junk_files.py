import os

def delete_junk_files(directory):
    junk_extensions = ['.tmp', '.bak', '.log', '.swp']  # Add more extensions if needed

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

    return deleted_files

def main():
    directory = input("Enter the directory to delete junk files: ")

    if os.path.isdir(directory):
        deleted_files = delete_junk_files(directory)

        if deleted_files:
            print("Junk files deleted:")
            for deleted_file in deleted_files:
                print(deleted_file)
        else:
            print("No junk files found.")
    else:
        print("Invalid directory. Please enter a valid directory path.")

if __name__ == "__main__":
    main()
