# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 08:31:24 2023

@author: rigel
"""

class NumbersList:
    # 1. Initiate for the Array
    def __init__(self, ArrayLength=100):
        self.Value = [0] * ArrayLength
        self.TopIndex = -1
        self.MaxIndex = ArrayLength - 1

    # 2. Function for Add Number
    def Append(self, Value):
        if self.TopIndex < self.MaxIndex:
            self.TopIndex = self.TopIndex + 1
            self.Value[self.TopIndex] = Value

    # 3. Print the List
    def Print(self):
        if self.TopIndex == -1:
            print("[] - The list is empty.")
            return
        print("[", end='')
        for i in range(self.TopIndex + 1):
            print(self.Value[i], end='')
            if i < self.TopIndex:
                print(", ", end='')
        print("]")

    # 4. Search the Index of the Number
    def Search(self, Value):
        SearchIndex = -1
        for i in range(self.TopIndex + 1):
            if self.Value[i] == Value:
                SearchIndex = i
                break
        return SearchIndex

    # 5. Delete Number
    def Delete(self, DeleteIndex):
        if self.TopIndex == -1:
            print("The list is empty. No numbers to delete.")
            return

        if DeleteIndex > self.TopIndex or DeleteIndex < 0:
            print("Invalid index. Deletion failed.")
            return

        for i in range(DeleteIndex, self.TopIndex):
            self.Value[i] = self.Value[i + 1]
        self.TopIndex = self.TopIndex - 1
        
    # 6. Check the List (if still there is number or not)
    def CheckList(self):
        if self.TopIndex == -1:
            return 1
    
    # 7. Reset the List
    def Reset(self):
        self.TopIndex = -1
        self.Value = [0] * (self.MaxIndex + 1)

##############
# MAIN PROGRAM
##############
a = NumbersList(100)
selectMenu = 1

print("\033[93m[LIST OF NUMBERS] - Using Array\033[0m\n")

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
                selectedNum = a.Search(int(selectNum))
    
                if selectedNum != -1:
                    a.Delete(selectedNum)
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
