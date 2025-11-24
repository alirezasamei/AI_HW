import json
from load_notes import load_notes

def save_note(note, filename):
    notes = load_notes(filename)
    notes.append(note)
    with open(filename,"w") as f:
        json.dump(notes, f, indent=4)
    
    