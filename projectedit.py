import pandas as pd
import time
import datetime

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
(25) Sort any numerical and non-numerical columns (Ascending or Descending):
(26) Print the first 100, 1000 or 5000 rows:
(27) Back to Main Menu
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
    global newdf
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
    df = df.drop(['Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street'],  axis='columns')
    newdf = pd.DataFrame(df)
    print(now.strftime("[%H:%M:%S]") + f" Total Columns Read: {len(df.columns)}")
    print(now.strftime("[%H:%M:%S]") + f" Total Rows Read:", len(newdf))
    print(f"\nFile loaded successfully! Time to load: {end_time-start_time:.2f} sec.")

def explore_data():
    while True:
        action = input(explore_menu + "\nPlease select an option: ")
        if action == "21":
            print("\nList of all columns:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]))
        elif action == "22":
            print(now.strftime("[%H:%M:%S]") + "\nSelect a column number to drop from the list:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            col_num = input(now.strftime("[%H:%M:%S]") + " ")
            col_name = df.columns[int(col_num)-1]
            df.drop(col_name, axis=1, inplace=True)
            print(now.strftime("[%H:%M:%S]") + f"\nColumn [{col_num}] {col_name} dropped!")
        elif action == "23":
            print("\nSelect column number to Describe:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            col_num = input(now.strftime("[%H:%M:%S]") + " ")
            print("Column " + col_num + " stats: \n============")
            if col_num == "1":
                break
        elif action == "25":
            print("How do you want to sort?")
            sort_order = input("(A)-Ascending or (D)-Descending: ")
            if sort_order == "A":
                print(df.sort_values(by=["year"], ascending=True))
                ascsort = df.sort_values(by=["year"], ascending=True)
                ascnum = 1
            elif sort_order == "D":
                print(df.sort_values(by=["year"], ascending=False))
                decsort = df.sort_values(by=["year"], ascending=False)
                decnum = 1
        elif action == "26":
            print("Choose 100, 1000, 5000 to print:")
            numprint = input(now.strftime("[%H:%M:%S]") + " ")
            if numprint == "100":
                print(df.head(n=100).to_string(index=False))
            if numprint == "1000":
                print(df.head(n=1000).to_string(index=False))
            if numprint == "5000":
                print(df.head(n=5000).to_string(index=False))
        elif action == "27":
            break
        else:
            print("\nInvalid option selected.")

# main program loop
while True:
    now = datetime.datetime.now()
    print(menu)
    action = input("Please select an option: ")
    if action == "1":
        load_data()
    elif action == "2":
        if df is None:
            print("\nPlease load a data set first!")
        else:
            explore_data()
    elif action == "4":
        print(newdf)
    elif action == "5":
        break
    else:
        print("\nInvalid option selected.")

