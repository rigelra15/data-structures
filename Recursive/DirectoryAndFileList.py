import os

def list_files(path, firstOptionPath, secondOptionPath, indentation=""):
    file = os.listdir(path)
    for item in file:
        # TO PRINT WITH PATH AND EXTENSION
        item_path = os.path.join(path, item)

        # TO PRINT WITH PATH BUT WITHOUT EXTENSION
        item_Path_WithoutExt = os.path.splitext(item_path)[0]

        # TO PRINT WITHOUT PATH BUT WITH EXTENSION
        item_NoPath_WithExt = os.path.basename(item_path)

        # TO PRINT WITHOUT PATH AND EXTENSION
        item_NoPath_WithoutExt = os.path.splitext(item_NoPath_WithExt)[0]

        # OPTION FOR SHOW WITH PATH OR NOT
        if firstOptionPath == "y":
            if secondOptionPath == "y":
                if os.path.isdir(item_path):
                    print(f"{indentation}\033[1;37;46m> Directory: {item_path}\033[0m")
                    list_files(item_path, firstOptionPath, secondOptionPath, indentation + "    ") # RECURSIVE HERE
                else:
                    print(f"{indentation}\033[0;32m>  File: {item_path}\033[0m")
            elif secondOptionPath == "n":
                if os.path.isdir(item_path):
                    print(f"{indentation}\033[1;37;46m> Directory: {item_Path_WithoutExt}\033[0m")
                    list_files(item_path, firstOptionPath, secondOptionPath, indentation + "    ") # RECURSIVE HERE
                else:
                    print(f"{indentation}\033[0;32m>  File: {item_Path_WithoutExt}\033[0m")

        elif firstOptionPath == "n":
            if secondOptionPath == "y":
                if os.path.isdir(item_path):
                    print(f"{indentation}\033[1;37;46m> Directory: {item_NoPath_WithExt}\033[0m")
                    list_files(item_path, firstOptionPath, secondOptionPath, indentation + "    ") # RECURSIVE HERE
                else:
                    print(f"{indentation}\033[0;32m>  File: {item_NoPath_WithExt}\033[0m")
            elif secondOptionPath == "n":
                if os.path.isdir(item_path):
                    print(f"{indentation}\033[1;37;46m> Directory: {item_NoPath_WithoutExt}\033[0m")
                    list_files(item_path, firstOptionPath, secondOptionPath, indentation + "    ") # RECURSIVE HERE
                else:
                    print(f"{indentation}\033[0;32m>  File: {item_NoPath_WithoutExt}\033[0m")

lastOption = "y"
while lastOption == "y":
    os.system('cls')
    print("\033[1;37;46mWelcome to FILE EXPLORER!\033[0m | By: Rigel R.")
    print("========================================")
    dir_path = input("Input Path: ")
    while not os.path.exists(dir_path):
        print(f"\033[1;37;41mThe specified path '{dir_path}' does not exist. Make sure you type it right!\033[0m")
        dir_path = input("Input Path: ")
    
    print(f"\033[1;37;42mThe specified path '{dir_path}' FOUND!\033[0m")
    print("=========================\n")
    print("\033[1;37;46mOPTIONS:\033[0m")
    firstOptionPath = input("> Do you want to print with the Path? (y/n): ")
    secondOptionPath = input("> Do you want to print with the Extension? (y/n): ")
    print("=========================\n")

    list_files(dir_path, firstOptionPath, secondOptionPath)

    lastOption = input("Try Again? (y/n): ")
print("Thanks for trying :D\n")