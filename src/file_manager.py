import os
from constants import MAGIC_NUMBER, HEADER_SIZE, BLOCK_SIZE

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
            magic_number = MAGIC_NUMBER
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
            if magic_number != MAGIC_NUMBER:
                print("Error: File is not a valid index file.")
                return None
            print(f"File '{file_name}' opened successfully.")
            return file_name
    except Exception as e:
        print(f"Error opening file: {e}")
        return None


def insert_into_index(file_name):
    if not file_name:
        print("No file is currently open. Please open an index file first.")
        return
    
    try:
        key = int(input("Enter the key (unsigned integer): ").strip())
        value = int(input("Enter the value (unsigned integer): ").strip())
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return
    
    try:
        with open(file_name, "r+b") as f:
            # Read the header
            f.seek(0)
            header = f.read(512)
            magic_number = header[:8]
            root_block_id = int.from_bytes(header[8:16], 'big')
            next_block_id = int.from_bytes(header[16:24], 'big')
            
            if magic_number != MAGIC_NUMBER:
                print("Error: File is not valid.")
                return
            
            # If no root exists, create the first node
            if root_block_id == 0:
                print("No root exists. Creating the root node.")
                f.seek(512)  # First block position
                root_node = create_btree_node(next_block_id, 0, [(key, value)], [])
                f.write(root_node)
                
                # Update the header
                root_block_id = next_block_id
                next_block_id += 1
                f.seek(8)
                f.write(root_block_id.to_bytes(8, 'big'))
                f.write(next_block_id.to_bytes(8, 'big'))
                print("Key-value pair inserted as root node.")
                return
            
            # Placeholder for handling existing root
            print(f"Inserting key {key} with value {value} into existing tree. Placeholder logic.")
    except Exception as e:
        print(f"Error during insertion: {e}")


def create_btree_node(block_id, parent_id, key_values, children):
    node = block_id.to_bytes(8, 'big')  # Block ID
    node += parent_id.to_bytes(8, 'big')  # Parent ID
    node += len(key_values).to_bytes(8, 'big')  # Number of key-value pairs
    
    # Add keys, values, and children (with padding)
    keys = [key for key, _ in key_values]
    values = [value for _, value in key_values]
    children_ids = children + [0] * (20 - len(children))  # Pad unused children
    
    node += b''.join(k.to_bytes(8, 'big') for k in keys) + b'\x00' * (152 - len(keys) * 8)
    node += b''.join(v.to_bytes(8, 'big') for v in values) + b'\x00' * (152 - len(values) * 8)
    node += b''.join(c.to_bytes(8, 'big') for c in children_ids)
    node += b'\x00' * (512 - len(node))  # Pad the node to 512 bytes
    return node


def load_btree(file_name):
    if not file_name:
        print("No file is currently open. Please open an index file first.")
        return None

    try:
        with open(file_name, "rb") as f:
            # Read the header
            f.seek(0)
            header = f.read(512)
            magic_number = header[:8]
            root_block_id = int.from_bytes(header[8:16], 'big')

            if magic_number != MAGIC_NUMBER:
                print("Error: File is not valid.")
                return None

            print(f"Loaded B-tree with root block ID {root_block_id}.")
            return root_block_id
    except Exception as e:
        print(f"Error loading B-tree: {e}")
        return None
