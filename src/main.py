# main.py

from file_manager import create_index_file, open_index_file
from btree import BTree

def print_menu():
    print("Commands:")
    print("create - Create a new index file")
    print("open   - Open an existing index file")
    print("insert - Insert a key/value pair into the index")
    print("search - Search for a key in the index")
    print("load   - Load key/value pairs from a file")
    print("print  - Print all key/value pairs in the index")
    print("extract - Extract all key/value pairs to a file")
    print("quit   - Exit the program")

def main():
    current_file = None
    current_btree = None
    while True:
        print_menu()
        command = input("Enter command: ").strip().lower()
        if command == "create":
            filename = input("Enter filename: ")
            if create_index_file(filename):
                current_file = filename
                current_btree = BTree(degree=10)
        elif command == "open":
            filename = input("Enter filename: ")
            if open_index_file(filename):
                current_file = filename
                current_btree = BTree(degree=10)
        elif command == "insert":
            if current_btree:
                key = int(input("Enter key: "))
                value = int(input("Enter value: "))
                current_btree.insert(key, value)
            else:
                print("No index file is open.")
        elif command == "search":
            if current_btree:
                key = int(input("Enter key: "))
                current_btree.search(key)
            else:
                print("No index file is open.")
        elif command == "load":
            if current_btree:
                filename = input("Enter filename to load: ")
                current_btree.load_from_file(filename)
            else:
                print("No index file is open.")
        elif command == "print":
            if current_btree:
                current_btree.print_tree()
            else:
                print("No index file is open.")
        elif command == "extract":
            if current_btree:
                filename = input("Enter filename to extract to: ")
                current_btree.extract_to_file(filename)
            else:
                print("No index file is open.")
        elif command == "quit":
            print("Exiting...")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
