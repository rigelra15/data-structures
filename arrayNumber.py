# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 08:31:24 2023

@author: rigel
"""

class NumbersList:
    def __init__(self, ArrayLength=100):
        self.Value = [0] * ArrayLength
        self.TopIndex = -1
        self.MaxIndex = ArrayLength - 1

    def Append(self, Value):
        if self.TopIndex < self.MaxIndex:
            self.TopIndex = self.TopIndex + 1
            self.Value[self.TopIndex] = Value

    def Print(self):
        if self.TopIndex == -1:
            print("[] - The list is empty.")
            print("")
            return
        print("[", end='')
        for i in range(self.TopIndex + 1):
            print(self.Value[i], end='')
            if i < self.TopIndex:
                print(", ", end='')
        print("]")

    def Search(self, Value):
        SearchIndex = -1
        for i in range(self.TopIndex + 1):
            if self.Value[i] == Value:
                SearchIndex = i
                break
        return SearchIndex

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
        
    def CheckList(self):
        if self.TopIndex == -1:
            return 1

a = NumbersList(100)
selectMenu = 1

print("[LIST OF NUMBERS] - Using Array")

inputMany = input("Type the desired number of numbers: ")
for i in range(int(inputMany)):
    inputNum = input("Type number: ")
    a.Append(int(inputNum))

while selectMenu != 2:
    print("")
    a.Print()

    print("Menu:")
    print("1. Delete a Number")
    print("2. Exit")

    selectMenu = input("Select: ")
    selectMenu = int(selectMenu)

    if selectMenu == 1:
        if a.CheckList() == 1:
            print("Sorry, but there are no more numbers to delete.")
        else:
            print("")
            a.Print()
            while True:
                selectNum = input("Select the number you want to delete: ")
                selectedNum = a.Search(int(selectNum))
    
                if selectedNum != -1:
                    a.Delete(selectedNum)
                    print("Number DELETED!")
                    break
    
                print("Number NOT FOUND!")

print("Thanks for trying!")
