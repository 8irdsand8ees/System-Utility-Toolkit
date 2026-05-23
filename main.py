import platform
import os


def system_info():
    print(platform.system())
    print(platform.version())


def file_list():
   print(os.listdir("."))


def create_note():

    note =input("Write your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved")


while True:

    print("\nTool Kit v0.3")
    print("1. System Info")
    print("2. File List")
    ptint("3. Create Note")
    print("4. Exit")

    choice =  input("> ")

    if choice == "1":
        system_info()

    elif choice =="2":
        file_list()

    elif choice == "3":
        create_note()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option")

