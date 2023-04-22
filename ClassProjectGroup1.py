#        Class: CMPS 3500
#        Leader:  Stephanie Esquivel
#        Student 2: Jose Chavez
#        Student 3: Steven Nez
#        Student 4: Nathan Nguyen
#        Date:  3/29/2023
#        File:  ClassProjectGroup1.py
#        Description:  
#        

#import numpy

#test csv read
import pandas as pd

#dataFrame = pd.read_csv('Crime_Data_from_2017_to_2019.csv')

#print("\nInput CSV file = \n", dataFrame)


#dataFrame['DR_NO']
#dataFrame['Date,']

#dataFrame.sort_values(["Reg_Price","Car"],axis=0, ascending=True,inplace=True,na_position='first')

#print("\nSorted CSV file (according to multiple columns) = \n", dataFrame)

import re

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

import csv

with open('Crime_Data_from_2017_to_2019.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)

    #for row in csvReader:
        #print(row[0])

#Sorting each 
#def quickSort():



#def Count():



#def UniqueCount():



#def Mean():

#array = numpy.array

#def Medium():



#def Mode():



#def SD():


#def Variance():



#def Minimum():



#def Maximum():



def main():
    #menuInput = None
    menuInput = menu()
    #backMenuInput = back_Menu()
    #loadDataMenuInput = loadData_Menu()
    #exploringDataMenuInput = exploringData_Menu()

    #menu()
    print(menuInput)
    while (menuInput !=1 or menuInput != 2 or menuInput != 3 or menuInput != 4):
        if menuInput == 1:
            loadData_Menu()
            #loadDataMenuInput() = loadData_Menu()
            #loadData_Menu()
            #back_Menu()
            menuInput = menu()
            #menuInput = None
            #exit()
        
        elif menuInput == 2:
            exploringData_Menu()
            #exploringData_Menu()
            menuInput = menu()

        elif menuInput ==3:
            dataAnalysis_Menu()
            menuInput = menu()
        elif menuInput == 4:
            printData_Set()
            exit()

        else:
            print("Please input a valid number")
            print(menuInput)
            #menuInput =None
            menuInput = menu()
            #menu()
        print (" menu input is " ,menuInput)
    print ("menu input is", menuInput)
        
#Our sorting function for the 
#def sort():


def loadData_Menu():
    def loadDataOutput():
        print(current_time,"")
        print(current_time,"")
        print(current_time,"")
        print("")
        print("File loaded successfully.")

    def crimedData2019():
        loadDataOutput()
        print("test1")
        #backMenu()
        
        

    def crimedData2021():
        loadDataOutput()
        print("test2")
        
    print("Load Data")
    print("********")
    print("Please Select an Option")
    print("[1] Crime_Data_from_2017_to_2019.csv")
    print("[2] Crime_Data_from_2020_to_2021.csv")
    print("Test.csv")
    while True:
        try:
            loadDataMenuInput = int(input(""))
            break
        except ValueError: 
            print("Please enter a valid number")
    #menuInput = int(input(""))
    #menuInput = (input(""))
    print(loadDataMenuInput)
    #return loadDataMenuInput
    while(loadDataMenuInput != 1 or loadDataMenuInput !=2):
        if(loadDataMenuInput ==1):
            crimedData2019()
            return

        elif (loadDataMenuInput == 2):
            crimedData2021()
            return

        else:
            print("")
            print("Print a valid number")
            loadDataMenuInput = loadData_Menu()
            exit()

    #return loadDataMenuInput
        print(current_time,"")
        print(current_time,"")
        print(current_time,"")
        print("")
        print("File loaded successfully.")
        print("Time to load ")
    return loadDataMenuInput

def exploringData_Menu():
    #define list,drop,describe, search column functions.
    def listAll_Columns():  ##21 
        print("List All the Columns")
        print("********")
        #Implement a loop to print out the column names
        print("")
        print("1) Column 1 Name")
        print("2) Column 2 Name")
        print("3) Column 3 Name")
        print("4) Column 4 Name ")
        print("...")


    def drop_Columns():  ##22
        print("Drop All the Columns")
        print("********")
        print("")
        #Implement a loop to print out the column names
        print("1) Column 1 Name")
        print("2) Column 2 Name")
        print("3) Column 3 Name")
        print("4) Column 4 Name ")
        print("...")

        while True:
            try:
                dropColumnsInput = int(input(""))
                break
            except ValueError: 
                print("Please enter a valid number")

        print(current_time, dropColumnsInput)
        print(current_time, "Columns", dropColumnsInput, " dropped")

    def describe_Columns(): ##23
        print("")
        print("Describe Columns")
        print(current_time, "Select a column to describe")

        #Implement a loop to print out the column names
        print("********")
        print("1) Column 1 Name")
        print("2) Column 2 Name")
        print("3) Column 3 Name")
        print("4) Column 4 Name ")
        print("...")

        while True:
            try:
                describeColumnsInput = int(input(""))
                break
            except ValueError: 
                print("Please enter a valid number")


        print("Column", describeColumnsInput, "stats")
        #Insert Column Stats after the word i.e. "Count",Count
        print("Count: ")
        print("Unique: ")
        print("Mean: ")
        print("Median: ")
        print("Mode:" )
        print("Standard Deviation: ")
        print("Variance: ")
        print("Minimum: ")
        print("Maximum: ")



    def searchElement_Columns():  ##24
        print("")
        print("Search Element in Column")
        print("********")
        print(current_time, "Select a column to search")
        print("********")
        print("1) Column 1 Name")
        print("2) Column 2 Name")
        print("3) Column 3 Name")
        print("4) Column 4 Name ")
        print("...")

        while True:
            try:
                searchElementColumnsInput = int(input(""))
                break
            except ValueError: 
                print("Please enter a valid number")


        print(searchElementColumnsInput)
        print("Enter an Element to Search")
        while True:
            try:
                searchElementInput = int(input(""))
                break
            except ValueError: 
                print("Please enter a valid number")
            
        print(current_time, searchElementInput)
        print(current_time)
        print(current_time)
        print("Search was successful! time to search was <Your Answer> sec.")

        print("")


    print("Exploring Data")
    print("********")
    print("(21) List all columns:")
    print("(22) Drop Columns:")
    print("(23) Describe Columns:")
    print("(24) Search Element in Column:")
    print("(25) Back to Main Menu")

    while True:
        try:
            exploringDataMenuInput = int(input(""))
            break
        except ValueError: 
            print("Please enter a valid number")

    while(exploringDataMenuInput != 21 or exploringDataMenuInput !=22 or  exploringDataMenuInput != 23
    or exploringDataMenuInput!= 24):
        if(exploringDataMenuInput ==21):
            listAll_Columns()
            return

        elif (exploringDataMenuInput == 22):
            drop_Columns()
            return
        
        elif (exploringDataMenuInput == 23):
            describe_Columns()
            return


        elif (exploringDataMenuInput == 24):
            searchElement_Columns()
            return

        else:
            print("")
            print("Print a valid number")
            exploringMenuInput = exploringData_Menu()
            exit()

    #exploringDataMenuInput = int(input(""))

    
    #menu()

def dataAnalysis_Menu():
    print("Data Analysis")
    print("********")
    print(current_time, "Show the total unique count of crimes per year sorted in descending order.")
    print(current_time, "Insert uniqueCount here")
    print("")

    print(current_time,"List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018 in West LA.")
    print(current_time, "Insrt Top5 Here")
    #dataAnalysisInput = input("")

def printData_Set():
    print("Insrt Data Set Here :)")

def back_Menu():
    print("Press any number to go back to main menu")
    while True:
        try:
            backMenuInput = int(input(""))
            break
        except ValueError: 
            print("Please enter a valid number")
    if backMenuInput == 4:
        menu()


def menu():
    

    print("Main Menu")
    print("*********")
    print("1.) Load Data")
    print("2.) Explore Data")
    print("3.) Data Analysis")
    print("4.) Print DataSet")
    print("4.) Quit")
    while True:
        try:
            menuInput = int(input(""))
            break
        except ValueError: 
            print("Please enter a valid number")
    #menuInput = int(input(""))
    #menuInput = (input(""))
    print(menuInput)
    return menuInput

main()

