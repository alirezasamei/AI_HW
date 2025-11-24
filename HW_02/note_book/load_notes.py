import json

def print_notes(filename):
    notes = load_notes(filename)
    for index, note in enumerate(notes):
        print(f"{index + 1} - {note}")

def load_notes(filename):
    try:
        with open(filename,"r") as f:
            return json.load(f)
    except:
        return []