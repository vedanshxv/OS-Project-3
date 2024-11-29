from file_manager import create_index_file, open_index_file, insert_into_index

def main():
    open_file = None  # Keeps track of the currently open file
    print("Welcome to the Index File Manager!")
    while True:
        print("\nMenu:")
        print("1. Create")
        print("2. Open")
        print("3. Insert")
        print("4. Search")
        print("5. Load")
        print("6. Print")
        print("7. Extract")
        print("8. Quit")
        
        command = input("\nEnter your command: ").strip().lower()
        
        if command == "create":
            create_index_file()
        elif command == "open":
            open_file = open_index_file()
        elif command == "insert":
            insert_into_index(open_file)
        elif command == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Command not implemented yet. Please try again.")

if __name__ == "__main__":
    main()
