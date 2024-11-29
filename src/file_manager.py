import os

def create_index_file():
    file_name = input("Enter the name of the new index file: ").strip()
    if os.path.exists(file_name):
        overwrite = input(f"The file '{file_name}' already exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite != "yes":
            print("File creation aborted.")
            return
    try:
        with open(file_name, "wb") as f:
            # Write the 512-byte header
            magic_number = b"4337PRJ3"
            root_block_id = (0).to_bytes(8, 'big')  # Tree is initially empty
            next_block_id = (1).to_bytes(8, 'big')  # Next block to be added
            header_padding = bytes(496)  # Padding to make 512 bytes
            f.write(magic_number + root_block_id + next_block_id + header_padding)
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

def open_index_file():
    file_name = input("Enter the name of the index file to open: ").strip()
    if not os.path.exists(file_name):
        print(f"The file '{file_name}' does not exist.")
        return None
    try:
        with open(file_name, "rb") as f:
            magic_number = f.read(8)
            if magic_number != b"4337PRJ3":
                print("Error: File is not a valid index file.")
                return None
            print(f"File '{file_name}' opened successfully.")
            return file_name
    except Exception as e:
        print(f"Error opening file: {e}")
        return None

