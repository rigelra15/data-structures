
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:35:18 2023

@author: rigel
"""

class NumbersList:
    # 1. Initiate for the List
    def __init__(self):
        self.Values = list()

    # 2. Function for Add Number
    def Append(self, Value):
        self.Values.append(Value)

    # 3. Print the List
    def Print(self):
        if len(self.Values) == 0:
            print(str(self.Values) + " - The list is empty.")
        else:
            print(self.Values)
    
    # def Search(self, Value):
    #     try:
    #         return self.Values.index(Value)
    #     except ValueError:
    #         return -1

    # 4. Delete Number
    def Delete(self, DeleteNumber):
        if DeleteNumber in self.Values:
            self.Values.remove(DeleteNumber)
            return True
        else:
            return False
        
        # if you use this, add function Search for find the Index
        # if 0 <= DeleteIndex < len(self.Values):
        #   del self.Values[DeleteIndex]
            
    # 5. Check the List (if still there is number or not)
    def CheckList(self):
        if len(self.Values) == 0:
            return 1
        
    # 6. Reset the List
    def Reset(self):
        self.Values.clear()

a = NumbersList()
selectMenu = 1

print("\033[93m[LIST OF NUMBERS] - Using List\033[0m\n")

# inputMany = input("Type the desired number of numbers: ")
# for _ in range(int(inputMany)):
#     inputNum = input("Type number: ")
#     a.Append(int(inputNum))

while selectMenu != 4:
    a.Print()

    print("Menu:")
    print("1. Delete Number")
    print("2. Add Number")
    print("3. Reset List")
    print("4. Exit")
    
    selectMenu = input("Select: ")
    selectMenu = int(selectMenu)

    # DELETE NUMBER
    if selectMenu == 1:
        if a.CheckList() == 1:
            print("Sorry, but there are no more numbers to delete.\n")
        else:
            print("")
            a.Print()
            while True:
                selectNum = input("Type the number you want to delete: ")
                if a.Delete(int(selectNum)):
                    print("\033[91mNumber DELETED!\033[0m") 
                    break
                
                print("\033[91mNumber NOT FOUND!\033[0m") 

    # ADD NUMBER
    elif selectMenu == 2:
        addManyNum = input("How many numbers do you want to add?: ")
        for i in range(int(addManyNum)):
            addNum = input(f"Type number ({i+1}): ")
            a.Append(int(addNum))
    
    # RESET LIST
    elif selectMenu == 3:
        a.Reset()
        print("\033[91mThe list has been reset!\033[0m\n")
        

print("Thanks for trying!")