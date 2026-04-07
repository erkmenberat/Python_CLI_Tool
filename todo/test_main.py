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

def test_in_file_writer(tmp_path):
    path = tmp_path / "sub"
    path.mkdir()
    file = path / "test.json"
    main.ensure_file(file)
    inhalt = ["yarrak"]
    main.save_todos(file, inhalt)
    result = main.load_todos(file)
    assert  result == ["yarrak"]

def test_ensure_logfile(tmp_path):
    path = tmp_path / "sub"
    path.mkdir()
    file = path / "logs.txt"
    main.ensure_logfile(file)
    check = False
    if file.exists():
        check = True
    assert check == True 

def test_error_logger(tmp_path): 
    path = tmp_path / "sub"
    path.mkdir()
    file = path / "logs.txt"
    try:
        raise ValueError("Fake error")
    except Exception as e:
        main.log_error(e, file)
    with open(file, "r") as log:
        inhalt = log.read()
    assert "Fake error" in inhalt






# def test_build_table():
    
#     assert 1 == 1
