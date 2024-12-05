# btree.py

class BTreeNode:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.keys = []       # Keys in this node
        self.values = []     # Corresponding values
        self.children = []   # Child nodes (if not a leaf)

class BTree:
    def __init__(self, degree):
        self.root = BTreeNode()  # Root of the B-Tree
        self.degree = degree     # Minimum degree of the B-Tree

    def insert(self, key, value):
        print(f"Inserting key: {key}, value: {value}")
        # Placeholder logic for B-Tree insertion
        if key in self.root.keys:
            print(f"Error: Key {key} already exists.")
            return
        self.root.keys.append(key)
        self.root.values.append(value)

    def search(self, key):
        print(f"Searching for key: {key}")
        # Traverse the root node for simplicity (does not handle multiple levels)
        if key in self.root.keys:
            index = self.root.keys.index(key)
            print(f"Key found: {key}, Value: {self.root.values[index]}")
        else:
            print(f"Key {key} not found.")

    def print_tree(self):
        print("B-Tree contents:")
        for key, value in zip(self.root.keys, self.root.values):
            print(f"Key: {key}, Value: {value}")

    def extract_to_file(self, filename):
        print(f"Extracting B-Tree contents to {filename}...")
        with open(filename, "w") as f:
            for key, value in zip(self.root.keys, self.root.values):
                f.write(f"{key},{value}\n")

    def load_from_file(self, filename):
        print(f"Loading key/value pairs from {filename}...")
        try:
            with open(filename, "r") as f:
                for line in f:
                    key, value = map(int, line.strip().split(","))
                    self.insert(key, value)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
