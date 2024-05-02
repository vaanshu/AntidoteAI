import os
from collections import defaultdict

def find_duplicates(directory):
    file_sizes = defaultdict(list)
    duplicate_files = []

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_size = os.path.getsize(file_path)
            file_sizes[file_size].append(file_path)

    for size, files in file_sizes.items():
        if len(files) > 1:
            duplicate_files.extend(files)

    return duplicate_files

def main():
    directory = input("Enter the directory to check for duplicate files: ")

    if os.path.isdir(directory):
        duplicates = find_duplicates(directory)

        if duplicates:
            print("Duplicate files found:")
            for duplicate in duplicates:
                print(duplicate)
        else:
            print("No duplicate files found.")
    else:
        print("Invalid directory. Please enter a valid directory path.")


if __name__ == "__main__":
    main()
