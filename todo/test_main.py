import pytest
import main

def test_todo_hinzufuegen():
    inhalt = []
    inhalt = main.todo_hinzufuegen(inhalt, "Neue Todo!")
    assert len(inhalt) == 1

def test_todo_entfernen():
    inhalt = []
    inhalt = main.todo_hinzufuegen(inhalt, "val")
    inhalt, gefunden  = main.todo_entfernen(inhalt, 'val')
    assert len(inhalt) == 0 and gefunden == True

