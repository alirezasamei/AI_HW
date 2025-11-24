from load_notes import load_notes

def search(searchparase, filename):
    searchresult = []
    index = 1
    notes = load_notes(filename)
    for note in notes:
        if(searchparase in note["title"] or searchparase in note["content"]):
            searchresult.append({
                "index": index,
                "title": note["title"],
            })
            index += 1
    return searchresult

def get_content_by_title(title, filename):
    notes = load_notes(filename)
    for note in notes:
        if note["title"] == title:
            return note["content"]