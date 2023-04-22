
import pandas as pd
import time

# define the menu options
menu = """
**********
(1) Load Data
(2) Exploring Data
(3) Data Analysis
(4) Print Data Set
(5) Quit
"""

# define the sub-menu options for exploring data
explore_menu = """
Exploring Data:
***************
(21) List all columns:
(22) Drop Columns:
(23) Describe Columns:
(24) Search Element in Column:
(25) Back to Main Menu
"""

# define the file options to load
file_options = """
Load data set:
**************
[1] Crime_Data_from_2017_to_2019.csv
[2] Crime_Data_from_2020_to_2021.csv
[3] Test.csv
"""

# initialize variables
df = None

# define functions for menu options
def load_data():
    global df
    file_num = input(file_options + "\nPlease select an option: ")
    filename = ""
    if file_num == "1":
        filename = "Crime_Data_from_2017_to_2019.csv"
    elif file_num == "2":
        filename = "Crime_Data_from_2020_to_2021.csv"
    elif file_num == "3":
        filename = "Test.csv"
    start_time = time.time()
    df = pd.read_csv(filename)
    end_time = time.time()
    print(f"\nFile loaded successfully! Time to load: {end_time-start_time:.2f} sec.")
    print(f"Total Columns Read: {len(df.columns)}")
    print(f"Total Rows Read: {len(df)}")

def explore_data():
    while True:
        action = input(explore_menu + "\nPlease select an option: ")
        if action == "21":
            print("\nList of all columns:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]))
        elif action == "22":
            col_num = input("\nSelect a column number to drop from the list:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            col_name = df.columns[int(col_num)-1]
            df.drop(col_name, axis=1, inplace=True)
            print(f"\nColumn [{col_num}] {col_name} dropped!")
        elif action == "25":
            break
        else:
            print("\nInvalid option selected.")

# main program loop
while True:
    print(menu)
    action = input("Please select an option: ")
    if action == "1":
        load_data()
    elif action == "2":
        if df is None:
            print("\nPlease load a data set first!")
        else:
            explore_data()
    elif action == "5":
        break
    else:
        print("\nInvalid option selected.")

