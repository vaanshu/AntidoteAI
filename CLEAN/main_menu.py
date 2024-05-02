import check_duplicates
import delete_junk_files

def main():
    print("Choose an option:")
    print("1. Check for duplicate files")
    print("2. Delete junk files")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        check_duplicates.main()
    elif choice == '2':
        delete_junk_files.main()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
