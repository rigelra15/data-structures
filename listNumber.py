
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:35:18 2023

@author: rigel
"""

class NumbersList:
    def __init__(self):
        self.Values = list()

    def Append(self, Value):
        self.Values.append(Value)

    def Print(self):
        if len(self.Values) == 0:
            print(self.Values, end='')
            print(" - The list is empty.")
        else:
            print(self.Values)

    def Delete(self, DeleteNumber):
        if DeleteNumber in self.Values:
            self.Values.remove(DeleteNumber)
            return True
        else:
            return False
            
    def CheckList(self):
        if len(self.Values) == 0:
            return 1

a = NumbersList()
selectMenu = 1

print("[LIST OF NUMBERS] - Using List")

inputMany = input("Type the desired number of numbers: ")
for _ in range(int(inputMany)):
    inputNum = input("Ketik angka: ")
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
            print("Sorry, but there are no more numbers to delete")
        else:
            print("")
            a.Print()
            while True:
                selectNum = input("Select the number you want to delete: ")
                if a.Delete(int(selectNum)):
                    print("Number DELETED!")
                    break
                
                print("Number NOT FOUND!")

print("Thanks for trying!")
