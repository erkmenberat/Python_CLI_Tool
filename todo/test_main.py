import pytest
import main
import json

CONTENT = "inhalt"

def test_todo_hinzufuegen():
    inhalt = []
    inhalt = main.todo_hinzufuegen(inhalt, "Neue Todo!")
    assert len(inhalt) == 1

def test_todo_entfernen():
    inhalt = []
    inhalt = main.todo_hinzufuegen(inhalt, "val")
    inhalt, gefunden  = main.todo_entfernen(inhalt, 'val')
    assert len(inhalt) == 0 and gefunden == True

def test_file_checker(tmp_path):
    path = tmp_path / "sub"
    path.mkdir()
    file = path / "test.json"
    main.ensure_file(file)
    with open(file, "r") as f:
        inhalt = json.load(f)
    assert inhalt == []

def test_file_loader(tmp_path):
    path = tmp_path / "sub"
    path.mkdir()
    file = path / "test.json"
    main.ensure_file(file)
    file.write_text('["yarrak"]')
    inhalt = main.load_todos(file)
    assert  inhalt == ["yarrak"]
