import platform
import os

while True:

    print("\nTool Kit v0.2")
    print("1. System Info")
    print("2. File List")
    print("3. Exit")

    choice =  input("> ")

    if choice == "1":
        print(platform.system())
        print(platform.version())

    elif choice =="2":
        print(os.listdir("."))

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid option")
