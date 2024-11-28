def main():
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
        
        if command == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Command not implemented yet. Please try again.")

if __name__ == "__main__":
    main()
