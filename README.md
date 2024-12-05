# OS-Project-3

This project implements a B-Tree index file system that supports key-value storage and efficient operations such as insertion, search, and bulk loading. The data is persisted using index files and can be interacted with through a command-line interface.

main.py: The main entry point of the application. Provides a command-line menu for managing index files and performing B-Tree operations.

btree.py: Contains the B-Tree and B-Tree node implementations. Includes logic for inserting, searching, printing, and extracting data from the B-Tree.

file_manager.py: Handles file-related operations, such as creating and opening index files, ensuring proper format and initialization.

constants.py: Defines constants used throughout the project, such as block size, magic number, and B-Tree degree.

devlog.md: A development log with notes about the progress and challenges encountered during the project.


To run the program, ensure all the provided files are in the correct directory structure. Navigate to the project directory in a terminal and run the program with the following command:

python3 src/main.py

Follow the on-screen menu to interact with the application.

create: Create a new index file.  
open: Open an existing index file.  
insert: Insert a key-value pair into the B-Tree.  
search: Search for a specific key and retrieve its value.  
load: Load key-value pairs from a file into the B-Tree.  
print: Display all key-value pairs currently stored in the B-Tree.  
extract: Export all key-value pairs to a file.  
quit: Exit the program.

