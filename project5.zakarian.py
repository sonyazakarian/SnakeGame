


"""
Sonya Zakarian
Project 5: A Simple Shell (File System Tree)

This project utilizes a Tree structure, with classes TreeNode and FileSystem, to create a navigable computer File System. 
In the main block, methods to modify/navigate the File System are called when corresponding strings are input to the Python terminal (e.g. "cd", "pwd).

"""

import pickle 

class TreeNode:

    def __init__(self, name, parent=None, is_directory=True):
        self.name = name 
        self.parent = parent
        self.is_directory = is_directory
        self.children = [] if is_directory else None

    def append_child(self, name, is_directory):
        if not self.is_directory:
            raise ValueError("Cannot append child to a file")
        new_child = TreeNode(name, parent=self, is_directory=is_directory)
        self.children.append(new_child)  # Add child to the children list
        return new_child

    def is_root(self):
        return self.parent is None

    def __str__(self):
        if self.is_directory:
            return f"{self.name} <directory>"
        else:
            return self.name
        

class FileSystem:
    def __init__(self):
        self.root = TreeNode(name="", parent=None, is_directory=True)
        self.current_directory = self.root

    def check_make_file(self,name):
        # Checks if child already exists
        for child in self.current_directory.children:
            if child.name == name:
                raise ValueError("Name already exists")

    def ls(self):
        for child in self.current_directory.children:
            print(child)

    def mkdir(self, dirname):
        # Adds new directory under current directory
        self.check_make_file(dirname) # Returns error if the directory already exists
        directory_child_node = TreeNode(dirname, parent=self.current_directory, is_directory = True)
        self.current_directory.children.append(directory_child_node)

    def touch(self, name):
        # Adds new file under current directory
        self.check_make_file(name) # Returns error if the file already exists
        file_child_node = TreeNode(name, parent=self.current_directory, is_directory = False)
        self.current_directory.children.append(file_child_node)

    def cd(self, name):
        if name == "..":
            # Sets current directory to parent, unless we are already at the root
            if self.current_directory.is_root():
                raise ValueError("Cannot move up. Already at the root directory.")
            self.current_directory = self.current_directory.parent
            return 
        
        for child in self.current_directory.children:
            # Sets current directory to child, as long as child exists and is a directory
            if child.name == name:
                if child.is_directory:
                    self.current_directory = child
                    return
                raise ValueError("You cannot cd to a file.")
        
        raise ValueError(f"No such child directory: '{name}'")

    
    def rm(self, filename):
        # Removes file under current directory
        for child in self.current_directory.children:
            if child.name == filename and not child.is_directory:
                self.current_directory.children.remove(child)
                return
        raise ValueError(f"File '{filename}' not found or is not a file.")

    def rmdir(self, dirname):
        # Removes directory under current directory
        for child in self.current_directory.children:
            if child.name == dirname and child.is_directory:
                self.current_directory.children.remove(child)
                return
        raise ValueError(f"Directory '{dirname}' not found or is not a directory.")


    def tree(self):
        def helper(node, level):
            # Print the current node with appropriate indentation
            print("\t" * level + str(node))
            
            # If the node is a directory, recursively print its children
            if node.is_directory:
                for child in node.children:
                    helper(child, level + 1)

        # Start the recursive traversal from the current directory
        helper(self.current_directory, 0)
    

    def pwd(self):
        path_components = [] # Stores path "components" from current dictionary up to the root
        current = self.current_directory 

        while current is not None:
            if current.name is not None: 
                path_components.append(current.name)
            current = current.parent  

        # Print path from root down to current directory, by reversing the order of the list
        print("/".join(path_components[::-1]))

def load_file_system():
    try:
        with open("file_system.bin", "rb") as file_source:
            file_system = pickle.load(file_source)
            print("File System loaded")
    except:
        print("Creating a new file system: file doesn't exist or data file is out of date because FileSystem class changed")
        file_system = FileSystem()
    return file_system
        
def save_file_system(file_system):
    with open("file_system.bin", "wb") as file_destination:
        pickle.dump(file_system, file_destination)
        print("File system saved")
    print("Finished")

def main():
    file_system = load_file_system()
    
    while True:  # File system shell runs until "quit"
        try:
            command = input(">> ").strip().split() # Split into command and arguments
            if not command:
                continue
            
            cmd = command[0] # cmd = actual command (e.g. rm)
            args = command[1:] # arg = argument that follows (e.g. filename)


            # Calls the corresponding method if user types the correct string in the terminal
            if cmd == "ls":
                file_system.ls()
            elif cmd == "pwd":
                file_system.pwd()
            elif cmd == "mkdir" and len(args) == 1:
                file_system.mkdir(args[0])
            elif cmd == "touch" and len(args) == 1:
                file_system.touch(args[0])
            elif cmd == "cd" and len(args) == 1:
                file_system.cd(args[0])
            elif cmd == "rm" and len(args) == 1:
                file_system.rm(args[0])
            elif cmd == "rmdir" and len(args) == 1:
                file_system.rmdir(args[0])
            elif cmd == "tree":
                file_system.tree()
            elif cmd == "quit":
                save_file_system(file_system) # Saves progress for next time
                print("Exiting the shell. Goodbye!")
                break
            else:
                print("Invalid command or arguments.")
        except Exception as e:
            # Prints exceptions, ensures program doesn't crash and continues to accept further commands
            print(f"Error: {e}")


if __name__ == "__main__":
    main()




    
