from file_manager import create_index_file, open_index_file, insert_into_index, load_btree
from btree import search_in_btree

def main():
    open_file = None
    root_block_id = None  # Keeps track of the current B-tree root

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
        elif command == "search":
            if open_file and root_block_id is not None:
                key = int(input("Enter the key to search for: ").strip())
                with open(open_file, "rb") as f:
                    search_in_btree(root_block_id, key, f)
            else:
                print("No file or B-tree loaded.")
        elif command == "load":
            if open_file:
                root_block_id = load_btree(open_file)
            else:
                print("No file is currently open. Please open a file first.")
        elif command == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Command not implemented yet. Please try again.")

if __name__ == "__main__":
    main()
