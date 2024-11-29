import struct

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
                print("Error: File is corrupted.")
                return
            
            # If no root exists, create the first node
            if root_block_id == 0:
                f.seek(512)  # Move to the first block position
                new_node = create_btree_node(next_block_id, 0, [(key, value)], [])
                f.write(new_node)
                
                # Update the header with the new root block
                root_block_id = next_block_id
                next_block_id += 1
                f.seek(8)
                f.write(root_block_id.to_bytes(8, 'big'))
                f.write(next_block_id.to_bytes(8, 'big'))
                print("Inserted key-value pair as the root node.")
                return
            
            # If the root exists, call placeholder B-tree logic
            print(f"Inserted key-value pair ({key}, {value}). (Placeholder logic)")
            
    except Exception as e:
        print(f"Error during insertion: {e}")

def create_btree_node(block_id, parent_id, key_values, children):
    # Helper to create a new node
    node = block_id.to_bytes(8, 'big')  # Block ID
    node += parent_id.to_bytes(8, 'big')  # Parent block ID
    node += len(key_values).to_bytes(8, 'big')  # Number of key-value pairs
    
    # Write keys and values
    keys = [key for key, _ in key_values]
    values = [value for _, value in key_values]
    children_ids = children + [0] * (20 - len(children))  # Pad with zeros for unused children
    
    node += b''.join(k.to_bytes(8, 'big') for k in keys) + b'\x00' * (152 - len(keys) * 8)
    node += b''.join(v.to_bytes(8, 'big') for v in values) + b'\x00' * (152 - len(values) * 8)
    node += b''.join(c.to_bytes(8, 'big') for c in children_ids)
    node += b'\x00' * (512 - len(node))  # Pad the node to 512 bytes
    return node
