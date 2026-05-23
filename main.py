import platform
import os


def system_info():
    print(platform.system())
    print(platform.version())


def file_list():
   print(os.listdir("."))


while True:

    print("\nTool Kit v0.3")
    print("1. System Info")
    print("2. File List")
    print("3. Exit")

    choice =  input("> ")

    if choice == "1":
        system_info()

    elif choice =="2":
        file_list()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid option")

