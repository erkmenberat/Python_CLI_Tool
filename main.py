import sys
import json
import traceback
import datetime
from pathlib import Path
from rich.console import Console
from rich.table import Table

date = str(datetime.datetime.now())
argv = sys.argv
argc = len(argv)
args = ["add", "rm", "ls", "--help"]

logs = Path.home() / "logs.txt"  # log file
jf   = Path.home() / "todos.json"  # jf == json file


# ── File Helpers ──────────────────────────────────────────────────────────────

def ensure_file(path): #DONE
    if not path.exists():
        path.write_text("[]")

def load_todos(path): #DONE
    with open(path, "r") as f:
        return json.load(f)

def save_todos(path, inhalt): #DONE
    with open(path, "w") as f:
        json.dump(inhalt, f)

def check_json():
    if not jf.exists():
        jf.write_text("[]")
        print("No Database found! --> Created todo.json")


# ── Todo Logic ────────────────────────────────────────────────────────────────

def todo_hinzufuegen(inhalt, userinput): #DONE
    inhalt.append({"ToDo": userinput})
    return inhalt

def todo_entfernen(inhalt, userinput): #DONE
    for i in inhalt:
        for val in i.values():
            if userinput == val:
                inhalt.remove(i)
                return inhalt, True
    return inhalt, False


# ── Display ───────────────────────────────────────────────────────────────────

def build_table(inhalt):
    table = Table(title="All Todos")
    table.add_column("Key")
    table.add_column("Value")
    for i in inhalt:
        for key, value in i.items():
            table.add_row(f"{key}", f"{value}")
    return table


# ── Error Logging ─────────────────────────────────────────────────────────────

def ensure_logfile(logfile):
    if not logfile.exists():
        logfile.write_text("Logs Created at: " + date + "\n\n")

def log_error(e, logfile):
    ensure_logfile(logfile)
    with open(logfile, "a") as log:
        traceback.print_exc(file=log)
        print("Fehler wurde geloggt.")
        print("Unbekannter Fehler: " + str(e) + " nur zu info Akhi. :/ ")
    return


# ── Commands ──────────────────────────────────────────────────────────────────

def add(userinput):
    try:
        ensure_file(jf)
        inhalt = load_todos(jf)
        inhalt = todo_hinzufuegen(inhalt, userinput)
        save_todos(jf, inhalt)
        ls()

    except PermissionError:
        print("Keine Berechtigung auf todos.json zuzugreifen!")

    except json.JSONDecodeError:
        print("Kaputte JSON Datei. --> " + str(jf) + " löschen und Programm neu Starten.")
        print("INFO: ToDos werden gelöscht!")

    except Exception as e:
        log_error(e, logs)

    return

def ls():
    try:
        ensure_file(jf)
        inhalt = load_todos(jf)
        console = Console()
        console.print(build_table(inhalt))

    except PermissionError:
        print("Keine Berechtigung auf todos.json zuzugreifen!")

    except json.JSONDecodeError:
        print("Kaputte JSON Datei. --> " + str(jf) + " löschen und Programm neu Starten.")
        print("INFO: ToDos werden gelöscht!")

    except Exception as e:
        log_error(e, logs)

    return

def rm(userinput):
    try:
        check_json()
        inhalt = load_todos(jf)
        inhalt, gefunden = todo_entfernen(inhalt, userinput)

        if gefunden: 
            save_todos(jf, inhalt)
            ls()
        else: 
            print("Todo nicht gefunden")

    except PermissionError:
        print("Keine Berechtigung auf todos.json zuzugreifen!")

    except json.JSONDecodeError:
        print("Kaputte JSON Datei. --> " + str(jf) + " löschen und Programm neu Starten.")
        print("INFO: ToDos werden gelöscht!")

    except Exception as e:
        log_error(e, logs)

    return

def rmall():
    try:
        inhalt = load_todos(jf)
        inhalt.clear()
        save_todos(jf, inhalt)
        ls()

    except Exception as e:
        log_error(e, logs)

def hilfe():  # help function DONE!
    # Just listing the Usage forms.
    print("Usage Main.Py: [add, delete, list, help]\n\n")
    print("These are the Commands that you can use: \n\n")
    print("     add <todo name>    Adds Todos that you can Check here throug 'list'\n")
    print("     ls     Lists all the Todos that you have written. \n")
    print("     rm <todo name>     Deletes the Selected Todo.\n")
    print("     help     Walkthrough for my very very Complex Commands.\n")
    return


# ── Routing ───────────────────────────────────────────────────────────────────

def arg(x):
    if x == args[0]:  # man kann noch nicht add -> mehr als ein wort machen. aber sonst funktioniert alles. es muss danach nur setup und test gemacht werden.
        if argc > 2:
            userinput = " ".join(argv[2:])  ## Better way to do that whats above.
            add(userinput)
        else:
            print("Undefinded arg: Usage: main.py help")
            return
    elif x == args[1]:
        if argc > 2:
            userinput = " ".join(argv[2:])  ## Better way to do that whats above.
            rm(userinput)
        else:
            rmall()
            return
    elif x == args[2]:
        ls()
    elif x == args[3]:
        hilfe()
    else:
        print("Hepinizin Amina Koymak lazim ama neyse.")
        return

def main():
    count = 0
    if argc > 1:  # no clue why this should work but it works :) dont touch it
        for i in args:
            if argv[1] == i:
                arg(i)
                return
            else:
                count += 1
            if count >= 4:
                print("Undefinded arg: Usage: main.py help")
                return
    else:
        hilfe()
        return

if __name__ == "__main__":
    main()
