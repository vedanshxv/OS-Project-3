# Development Log

## Nov 27, 12:44 PM 
### Initial Thoughts  
- This project involves creating an interactive program to manage index files using a B-Tree structure.  
- I need to implement commands like `create`, `open`, `insert`, `search`, and others as outlined in the project details.  
- The B-Tree will have a minimal degree of 10 and must be stored in blocks of 512 bytes, using a specific header format.  
- All operations must handle user input errors 
### Plan  
- Begin by setting up the basic structure of the program, focusing on the interactive menu and handling user input.  
- Implement file creation and opening functionality as the first features.  
- Keep development incremental and ill log all updates as I go

My thoughts in general:

The requirement to manage index files with only three nodes in memory at a time feels like it could be tricky, so I’ll need to carefully plan how to handle memory efficiently. Understanding the file structure, particularly with the big-endian byte order, will be important to get right early on. For now, my main focus will be on implementing the create and open commands to establish the foundation for the program.


## Nov 28, 5:52 PM 

Today, I began working on the foundation of the program by implementing the basic structure and an interactive menu. My focus was on creating a simple user interface that displays the available commands and handles user input. For now, I’ve only implemented the quit command to allow users to exit the program, while other commands display a placeholder message or I mgiht just keep it completely empty. This was a good starting point to get a feel for the program flow and ensure that the menu is user-friendly. I’m feeling good about the progress so far as the skeleton of the program is functional and ready for further development. Moving forward, I plan to implement the create and open commands.

## Nov 28, 10:36 PM

I implemented the foundational functionality for managing index files. The create_index_file function creates new index files with a properly formatted 512-byte header, ensuring existing files are not overwritten without confirmation. The open_index_file function opens and validates index files by checking their magic number for integrity. These commands establish the core file management operations for the rest of the project.

Thoughts so far: Managing binary files with proper validation has been insightful. I feel more confident working with file structures and understanding the importance of error handling. This step also highlighted the need for careful planning of B-tree operations moving forward.

What I planned to accomplish this session: My goal was to implement the create and open commands to handle file creation and validation.

Reflection on the session: I achieved my goal and tested the functionality thoroughly. Handling binary data and ensuring robust validation were challenges, but I now feel prepared to tackle the next steps.

What I plan to do next: I plan to implement the insert command to add key-value pairs to the B-tree and save them to the index file efficiently.

## Nov 29, 12:03 PM


Before starting this session, I reviewed the requirements for implementing the insert command. My thoughts so far are that the project is becoming more complex as I move into operations involving the B-tree structure, but the initial groundwork on file management will make this manageable.  

For this session I plan to implement insert command. My goal is to allow users to add key-value pairs into the index file, initializing the root node if it doesn't exist and setting up placeholder logic for future node handling. This will help prepare the structure for full B-tree operations in next coding sesisons.