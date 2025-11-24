from datetime import datetime
import os
from pprint import pprint
from save_note import save_note
from load_notes import print_notes
import search
from delete_note import delete_note

filename = "notes.JSON"

while True:
    try:
        os.system("cls")
        action = input("choose:\n1 - create note\n2 - show notes\n3 - search in notes\n4 - delete a note\n5 - exit\n")
        os.system("cls")
        match(action):
            case "1":
                print("___create note___")
                title = input("enter the tilte: \n")
                content = input("enter the content: \n")
                date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                note = {
                    "title" : title,
                    "date" : date,
                    "content" : content,
                }
                save_note(note, filename)
            case "2":
                    print("___show notes___")
                    print_notes(filename)
                    input("press anything to continue")
            case "3":
                print("____search in notes___")
                searchphrase = input("enter a part of what are you looking for: ")
                os.system("cls")
                titles = search.search(searchphrase, filename)
                if len(titles) == 0:
                    print("nothing found!")
                    input("press anything to continue")
                    continue
                strtitleslist = "".join([f"{title['index']:^5} - \"{title['title']}\"\n" for title in titles])
                yn = "y"
                while yn == "y" or yn == "Y":
                    os.system("cls")
                    print(F"looking for {searchphrase} in notes:")
                    print("index - title")
                    print("".join(strtitleslist))
                    index = int(input("enter note index to show content: "))
                    content = search.get_content_by_title(titles[index-1]["title"],filename)
                    print(f"\n{content}\n")
                    yn = input("do you want to show an other note content? y/n: ")
            case "4":
                print("___delete note___")
                print_notes(filename)
                index = int(input("choose one of the notes by its row number: "))
                delete_note(index, filename)
            case "5":
                  break
    except Exception as e:
        pprint(e)
        input("press anything to continue") 
        continue            
