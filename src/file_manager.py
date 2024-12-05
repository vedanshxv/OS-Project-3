# file_manager.py

import os
from constants import MAGIC_NUMBER, BLOCK_SIZE

def create_index_file(filename):
    if os.path.exists(filename):
        overwrite = input(f"{filename} already exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite != "yes":
            print("Operation aborted.")
            return False
    with open(filename, "wb") as f:
        header = MAGIC_NUMBER + (0).to_bytes(8, 'big') + (1).to_bytes(8, 'big')
        f.write(header.ljust(BLOCK_SIZE, b'\x00'))
    print(f"{filename} created successfully.")
    return True

def open_index_file(filename):
    if not os.path.exists(filename):
        print(f"{filename} does not exist.")
        return None
    with open(filename, "rb") as f:
        header = f.read(BLOCK_SIZE)
        if header[:8] != MAGIC_NUMBER:
            print(f"{filename} is not a valid index file.")
            return None
    print(f"{filename} opened successfully.")
    return filename
