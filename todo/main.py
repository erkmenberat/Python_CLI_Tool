import sys
from pathlib import Path

argv = sys.argv 
argc = len(argv)
args = ["add", "delete", "list", "help"]

def main():
    count = 0
    if(argc < 3):
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
        print("Wrong input: Usage --> arg arg : add sex")
        return


def arg(x):
    if(x == args[0]):
        print("i am adder.")
    elif(x == args[1]):
        print("del")
    elif(x == args[2]):
        print("list")
    elif(x == args[3]):
        hilfe()
    else:
        print("Hepinizin Amina Koymak lazim ama neyse.")
        return


def add():
    # add todo into a json data check if the json file is existin or not. --> Learn how to do that Berat
    return

def delete():
    # Check how to edit a JSON file using pyhton
    return

def ls():
    # Check how to Print a Json file on Terminal in Python? 
    return

def hilfe():
    #Just listin the Usage forms. 
    print("Usage Main.Py: [add, delete, list, help]\n\n")
    print("These are the Commands that you can use: \n\n")
    print("     add     Adds Todos that you can Check here throug 'list'\n")
    print("     list     Lists all the Todos that you have written. \n")
    print("     delete <todo name>     Deletes the Selected Todo.\n")
    print("     help     Walkthrough for my very very Complex Commands.\n")
    return


main()




    # if(args[num] == "add"):
    #     add()
    # elif(args[num] == "delete"):
    #     delete()
    # elif(args[num] == "list"):
    #     ls()
    # elif(args[num] == "help"):
    #     hilfe()