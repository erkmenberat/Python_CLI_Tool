import sys
from pathlib import Path
import json 
import traceback 
import datetime

date = str(datetime.datetime.now())
argv = sys.argv 
argc = len(argv)
args = ["add", "rm", "ls", "--help"] ### args müssen richtig definded werden und sie funktunieren noch nicht als diese art von eingabe add [...] ls - 
#status = False commented out because if a Todo is finished the user should delete it.

logs = Path.home() / "logs.txt" #log file
jf = Path.home() / "todos.json" #jf == json file

def main():
    count = 0
    if(argc > 1 & argc < 3): # no clue why this should work but it works :) dont touch it
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
    
def arg(x):
    if(x == args[0]):# man kann ncoh nicht add -> mehr als ein wort machen. aber sonst funktuniert alles. es muss danach nur setup und test gemacht werden. 
        if(argc > 2):
            fakearr = []
            for i in range(2, argc):
                fakearr.append(argv[i])

            userinput = " ".join(fakearr)
            add(userinput)
        else:
            print("Undefinded arg: Usage: main.py help")
            return
    elif(x == args[1]):
        if(argc > 2):
            fakearr = []
            for i in range(2, argc):
                fakearr.append(argv[i])

            userinput = " ".join(fakearr)
            rm(userinput)
        else:
            print("Undefinded arg: Usage: main.py help")
            return
    elif(x == args[2]):
        ls()
    elif(x == args[3]):
        hilfe()
    else:
        print("Hepinizin Amina Koymak lazim ama neyse.")
        return

def add(input):# add function DONE!

    if not jf.exists(): # check if the file is existing
        jf.write_text("[]") # if not create a empty file. 

    with open(jf, "r") as f:  # using "with" for safety it is closing the file automaticly after opening. 
        inhalt = json.load(f) # saving into inhalt the value of opened file -> todo.json

    inhalt.append({"ToDo": input}) # Add the Infos into the JSON file. 

    with open(jf, "w") as f: 
        json.dump(inhalt, f) # its opening the json file and writing the changes into the file. 

    print("Succesfully Added " + input) # info

    return

def ls(): # List Function DONE!
    # Check how to Print a Json file on Terminal in Python? 

    try:
        if not jf.exists(): # check if the file is existing
            jf.write_text("[]") # if not create a empty file.
            print("No Database found! --> Created todo.json") #alerting
        
        with open(jf, "r") as f:  # using "with" for safety it is closing the file automaticly after opening. 
            inhalt = json.load(f) # saving into inhalt the value of opened file -> todo.json

        for i in inhalt: # inhalt [´{example1}, {example2}] i = {example1} --> {example2}.
            for x, y in i.items(): # gets the key and the values thats .items() :) 
                print(f"{x}: {y}") # prints out only the key and value ;) 
    
    except json.JSONDecodeError:
        print("Kaputte JSON Datei. --> " + str(jf) + " löschen und Programm neu Starten.") 
        print("INFO: ToDos werden gelöscht!")       

    except Exception as e:
        if not logs.exists(): 
            logs.write_text("Logs Created at: " + date + "\n\n")
    
        with open(logs, "a") as log: 
            traceback.print_exc(file=log)
            print("Fehler wurde geloggt.") 

        print("Unbekannter Fehler: " + str(e) + " nur zu info Akhi. :/ ")
         
    return

def rm(input): # rm command DONE!
    # Check how to edit a JSON file using pyhton
    # use clear()
    index = 0 # for the loop index
    
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