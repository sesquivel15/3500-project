import pandas as pd
import time
import datetime

''' _________ Functions and Names _____________

Now = Current time
Count(iterable)  ---  = counter
UniqueCount(iterable) = Unique Count
Mean(arr)  --------   = Mean of arr
Median(arr)  -------  = Median of arr
Mode(arr) =  -------  = Mode of arr
square_root(value)    = Used for SD, finding square root
SD(arr) =  ---------  = Standard Deviation 
Variance(arr)  -----  = Variance of arr
Min(arr) =   ------   = Finding Minimum
Max(arr) =   ------   = Finding Maximum

'''

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
# ------------------- define functions for menu options -----------------------------

def load_data():

    global df
    # _______________ Selecting which .csv file to open _______
    file_num = input(file_options + "\nPlease select an option: ")
    filename = ""

    if file_num == "1":
        filename = "Crime_Data_from_2017_to_2019.csv"
    elif file_num == "2":
        filename = "Crime_Data_from_2020_to_2021.csv"
    elif file_num == "3":
        filename = "Test.csv"

    # __________ File Read Time _________
    start_time = time.time()
    df = pd.read_csv(filename)
    end_time = time.time()

    df = df.drop(['Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street'],  axis='columns')
    newdf = pd.DataFrame(df)

    # -------------------------- Print Statements -----------------------------
    print(newdf)
    print(now.strftime("[%H:%M:%S]") + f" Total Columns Read: {len(df.columns)}")
    print(now.strftime("[%H:%M:%S]") + f" Total Rows Read:", len(newdf))
    print(f"\nFile loaded successfully! Time to load: {end_time-start_time:.2f} sec.")
    
    # _________________________ Exploring Data Section __________________
def explore_data():
    while True:
        action = input(explore_menu + "\nPlease select an option: ")

        #____________ (21) Listing all the columns from the file _____________
        if action == "21":
            print("\nList of all columns:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]))
        
        #___________________ (22) Select a column to drop __________________
        elif action == "22":
            print(now.strftime("[%H:%M:%S]") + "\nSelect a column number to drop from the list:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            col_num = input(now.strftime("[%H:%M:%S]") + " ")
            col_name = df.columns[int(col_num)-1]
            df.drop(col_name, axis=1, inplace=True)
            print(now.strftime("[%H:%M:%S]") + f"\nColumn [{col_num}] {col_name} dropped!")

        #___________________ (23) Describe specified column data ____________________
        elif action == "23":
            print("\nSelect column number to Describe:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            col_num = input(now.strftime("[%H:%M:%S]") + " ")
            print("Column " + col_num + " stats: \n============")
            if col_num == "1":
                nums = df.count()[1]
                nums == df[df.columns[1]].count()
                print("Count: ", nums)
            
        # __________________ (25) Quit MENU _____________________-
        elif action == "25":
            break
        else:
            print("\nInvalid option selected.")

# -------------------- main program loop --------------------
while True:
    #______ Current time _______
    now = datetime.datetime.now()

    # ____________ User selects an option _________
    print(menu)
    action = input("Please select an option: ")

    # ______________ Load data from dataset _______
    if action == "1":
        load_data()

    # _______________ Dataset isn't loaded ______
    elif action == "2":
        if df is None:
            print("\nPlease load a data set first!")
        else:
            explore_data()
    # __________________ Quit __________
    elif action == "5":
        break
    else:
        print("\nInvalid option selected.")


# ________________ Sorting Functions _____________

#_______ Counting rows function ________
def Count(iterable):
    count = 0
    for row in iterable:
        count += 1
    return count

#_______ Counting Unique Items _______
def UniqueCount(iterable):
    unique_rows = set()
    for row in iterable:
        # Assuming row is a list or tuple, convert it to a string to make it hashable
        row_string = str(row)
        unique_rows.add(row_string)
    return len(unique_rows)

#________ Determining the Mean of given item ________
def Mean(arr):
    return sum(arr) / len(arr)

# _______ Median of given item _______
def Median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

# ________ Mode of given item ______
def Mode(arr):
    count_dict = {}
    for item in arr:
        count_dict[item] = count_dict.get(item, 0) + 1
    max_count = max(count_dict.values())
    return [item for item, freq in count_dict.items() if freq == max_count]

# _______ Used in Standard Deveation function ______
def square_root(value):
    return value ** 0.5

# _______ Standard Deviation of Item_______
def SD(arr):
    mean = Mean(arr)
    return square_root(sum([(x - mean)**2 for x in arr]) / len(arr))

#________ Measure of Variability _______
def Variance(arr):
    return SD(arr)**2

#________ Finding Minimum ______
def Min(arr):
    return min(arr)

#________ Finding Maximum ______
def Maximum(arr):
    return max(arr)

