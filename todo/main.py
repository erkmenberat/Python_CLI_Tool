import sys
from pathlib import Path
import json 

argv = sys.argv 
argc = len(argv)
args = ["add", "rm", "ls", "help"]
#status = False commented out because if a Todo is finished the user should delete it.

def main():
    count = 0
    if(argc > 1 & argc < 3):
        for i in args: 
            if(argv[1] == i):
                arg(i)
                return
            else:
                count += 1
                if(count >= 4):
                    print("Undefinded arg: Usage: main.py help")
                    return
    else:
        hilfe()
        return

def arg(x): # must be changed but works fine rn
    if(x == args[0]):
        userinput = input("Todo you wanna add: ")
        add(userinput)
    elif(x == args[1]):
        userinput = input("Todo you wanna remove: ") # shoud have a fallback if there is no todo that name exist at all
        rm(userinput)
    elif(x == args[2]):
        ls()
    elif(x == args[3]):
        hilfe()
    else:
        print("Hepinizin Amina Koymak lazim ama neyse.")
        return

def add(input):# add function DONE!

    jf = Path.home() / "todos.json" #jf == json file
    
    if not jf.exists(): # check if the file is existing
        jf.write_text("[]") # if not create a empty file. 

    with open(jf, "r") as f:  # using "with" for safety it is closing the file automaticly after opening. 
        inhalt = json.load(f) # saving into inhalt the value of opened file -> todo.json

    inhalt.append({"ToDo": input}) # Add the Infos into the JSON file. 

    with open(jf, "w") as f: 
        json.dump(inhalt, f) # its opening the json file and writing the changes into the file. 

    return

def ls(): # List Function DONE!
    # Check how to Print a Json file on Terminal in Python? 

    jf = Path.home() / "todos.json" #jf == json file
    
    if not jf.exists(): # check if the file is existing
        jf.write_text("[]") # if not create a empty file.
        print("No Database found! --> Created todo.json") #alerting
    
    with open(jf, "r") as f:  # using "with" for safety it is closing the file automaticly after opening. 
        inhalt = json.load(f) # saving into inhalt the value of opened file -> todo.json

    for i in inhalt: # inhalt [´{example1}, {example2}] i = {example1} --> {example2}.
        for x, y in i.items(): # gets the key and the values thats .items() :) 
            print(f"{x}: {y}") # prints out only the key and value ;) 
    
    return

def rm(input): # rm command DONE!
    # Check how to edit a JSON file using pyhton
    # use clear()
    index = 0 # for the loop index

    jf = Path.home() / "todos.json" #jf == json file
    
    if not jf.exists(): # check if the file is existing
        jf.write_text("[]") # if not create a empty file.
        print("No Database found! --> Created todo.json") #alerting
    
    with open(jf, "r") as f:  # using "with" for safety it is closing the file automaticly after opening. 
        inhalt = json.load(f) # saving into inhalt the value of opened file -> todo.json

    for i in inhalt: # i is the hole Todo Data key + value 
        for val in i.values(): # val is only the values from the todos. 
            if(input == val): # basic english
                inhalt.remove(i) # removes the i which is the hole Todo index key + value
                print("Succesfully Removed Todo") # info
                with open(jf, "w") as f: 
                    inhalt = json.dump(inhalt, f) # writes the changes in the file
                return
            else: # if there is no todo like the input
                 if(index >= len(inhalt)-1): # checks for the index length just for going trough all the todos. inhalt -1 because inhalt lenth starts from 1 but index from 0. 
                     print("There is no Todo like this!?") # if all the todos are seen print this info an return nothning. 
                     return
                 index += 1 # index = 0 --> index = 1 because first index was seen. 

def hilfe(): # help function DONE!
    #Just listin the Usage forms. 
    print("Usage Main.Py: [add, delete, list, help]\n\n")
    print("These are the Commands that you can use: \n\n")
    print("     add <todo name>    Adds Todos that you can Check here throug 'list'\n")
    print("     ls     Lists all the Todos that you have written. \n")
    print("     rm <todo name>     Deletes the Selected Todo.\n")
    print("     help     Walkthrough for my very very Complex Commands.\n")
    return

main()