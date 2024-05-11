import os

list = "list.txt"

def clear_file(): # clears out contents of file
    todo = open(list, "w")
    todo.close()

def read_file(): # prints out the file
    todo = open(list, "r")
    clear_screen()
    print(todo.read())

def reset_screen():
    clear_screen()
    read_file()

def clear_screen(): # clears the terminal
    os.system("cls")

def add_line(line): # adds a new line to the list
    todo = open(list, "a")
    todo.write(line + "\n")
    todo.close()

def remove_line(message): # removes a line
    with open(list, "r") as todo: # open as read
        lines = todo.readlines() # create list of lines

    mod_lines = [line.replace(message + "\n", "") for line in lines] # create new list without line

    with open(list, "w") as todo: # open as write
        todo.writelines(mod_lines) # replace file with new list
    todo.close() # close file

def run_list(): # runs the list until stopped
    running = True

    reset_screen()

    while running:
        message = input()

        if message.lower() == "clear": # clears contents of file
            clear_file()
            reset_screen()

        elif "add " in message:
            message = message.replace("add ", "") # add a line to file
            add_line(message)
            reset_screen()
            
        elif "remove " in message: # remove a line to file
            message = message.replace("remove ", "")
            remove_line(message)
            reset_screen()

        elif message.lower() == "quit": # exit out of file
            running = False

    read_file()

def main():
    run_list()

main()