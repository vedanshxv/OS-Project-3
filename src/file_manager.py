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
            
            if magic_number != b"4337PRJ3":
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
 
