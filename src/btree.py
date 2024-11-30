class BTreeNode:
    def __init__(self, block_id, parent_id):
        self.block_id = block_id
        self.parent_id = parent_id
        self.keys = []  # Keys in the node
        self.values = []  # Values corresponding to the keys
        self.children = []  # Child block IDs

    def is_full(self, max_keys=20):
        return len(self.keys) >= max_keys


def split_node(node, next_block_id):
    print(f"Splitting node {node.block_id}.")
    left_node = BTreeNode(next_block_id, node.parent_id)
    right_node = BTreeNode(next_block_id + 1, node.parent_id)
    return left_node, right_node


def search_in_btree(root_block_id, key, file_handle):
    if root_block_id == 0:
        print("Tree is empty. Key not found.")
        return None

    current_block_id = root_block_id
    while current_block_id != 0:
        file_handle.seek(current_block_id * 512)
        node_data = file_handle.read(512)

        num_keys = int.from_bytes(node_data[16:24], 'big')
        keys = [int.from_bytes(node_data[24 + i * 8:32 + i * 8], 'big') for i in range(num_keys)]
        values = [int.from_bytes(node_data[176 + i * 8:184 + i * 8], 'big') for i in range(num_keys)]

        for i, existing_key in enumerate(keys):
            if key == existing_key:
                print(f"Key {key} found with value {values[i]}.")
                return values[i]
            if key < existing_key:
                current_block_id = int.from_bytes(node_data[376 + i * 8:384 + i * 8], 'big')
                break
        else:
            current_block_id = int.from_bytes(node_data[376 + num_keys * 8:384 + num_keys * 8], 'big')

    print(f"Key {key} not found.")
    return None
