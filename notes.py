def create_note():
    not - input("Write your note: ")

    with open("notes.txt", "ra")  as f:
       f.write(not + "\n")

    print("Note saved")


def read_notes():
    try:
        with open("notes.txt", "r") as f:
           print(f.read())
    except FileNotFoundError:
        print("NO notes found")
