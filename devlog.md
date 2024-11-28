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

Today, I began working on the foundation of the program by implementing the basic structure and an interactive menu. My focus was on creating a simple user interface that displays the available commands and handles user input. For now, I’ve only implemented the quit command to allow users to exit the program, while other commands display a placeholder message or I mgiht just keep it completely empty. This was a good starting point to get a feel for the program flow and ensure that the menu is user-friendly. I’m feeling good about the progress so far as the skeleton of the program is functional and ready for further development. Moving forward, I plan to implement the create and open commands
