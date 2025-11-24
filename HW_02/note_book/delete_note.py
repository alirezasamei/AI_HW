import json
from load_notes import load_notes


def delete_note(index, filename):
    notes = load_notes(filename)
    del notes[index-1]
    with open(filename,"w") as f:
        json.dump(notes, f, indent=4)