# opening and creating files with the open method
# file methods are cursors, we need to be always mindful of where the cursor is

# without the with mehtod > my_file = open(r'100 Days Challenges\Day 24 - High Score for Snake Game\my_file.txt', 'r+')
with open(r'..\..\my_file.txt', 'w+') as my_file: # the ..\ signifies going back from the selected file path, so it is relative to the file itself instead of relative to the working directory.
    my_file.write('hi. this is me testing opening, writing and closing files using python.')

    my_file.seek(0) # << rewind the cursor to the start; write() left it at the end of the file
    contents = my_file.read()
    print(contents)

# my_file.close() # << if we are not using the with method, we need to manually close the file to free up resources.

# keep in mind the mode of the file that you open. For all the modes and their properties, read the documentaion: https://docs.python.org/3/builtins/functions.html#open
