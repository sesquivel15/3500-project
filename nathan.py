#        Class: CMPS 3500
#        Leader:  Stephanie Esquivel
#        Student 2: Jose Chavez
#        Student 3: Steven Nez
#        Student 4: Nathan Nguyen
#        Date:  3/29/2023
#        File:  ClassProjectGroup1.py
#        Description:  
#   
import pandas as pd
import time
import datetime
import numpy as np

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

def da1(df):
    sorted_df = df.sort_values(by=column_name, ascending=False)

def dataAnalysis():
    print("Show the total unique count of crimes per year sorted in descending order")
    print("hot the top 5 areas (AREA NAME) with the mos crime events in all years (Sorted by the number of crime events)")
    print("Show all months and the unique total count of crimes sorted in increasing order.")



# initialize variables
df = None

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
    print ('test',df)
    

    # -------------------------- Print Statements -----------------------------
   
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
            print(now.strftime("[%H:%M:%S]") + f" Column [{col_num}] {col_name} dropped!")

#___________________ (23) Describe specified column data ____________________
        
        elif action == "23":
         #   print("\nSelect column number to Describe:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
          #  col_num = input(now.strftime("[%H:%M:%S]") + " ")
           # print("Column " + col_num + " stats: \n============")
            #col_num = int(col_num)
           # if col_num > 0:
            #    column2_stats = df['col_num'].describe()
             #   print(column2_stats)
            print("\nSelect column number to Describe:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            col_num = int(input(now.strftime("[%H:%M:%S]") + " "))
            print("Column " + str(col_num) + " stats: \n============")
            if col_num > 0 and col_num <= len(df.columns):
                column_name = df.columns[col_num - 1]
                column_stats = df[column_name].describe()
                print(column_stats)
            else:
                print("Invalid column number. Please try again.")
# ______________ (24) Search for Specific Element ____________________
        elif action == "24":
            print("\nSelect column number to search within:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            col_num = int(input(now.strftime("[%H:%M:%S]") + " "))
            if col_num > 0 and col_num <= len(df.columns):
                column_name = df.columns[col_num - 1]
                search_query = input("Enter the element(s) to search for (separated by commas for multiple values): ")
                search_values = [value.strip() for value in search_query.split(",")]
                search_results = df[df[column_name].isin(search_values)].index.tolist()
            if len(search_results) > 0:
                print(f"\nSearch Results in column '{column_name}':")
                print(f"Element found in rows: {search_results}")
            else:
                print(f"\nNo results found in column '{column_name}'.")
        #else:
         #   print("Invalid column number. Please try again.")
# ______ (25) Sort Columns in either Ascending or Descending ___________
        elif action == "25":
            print("Which column do you want to sort?" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]))
            column_num = int(input("Enter the column number: "))
            if column_num < 1 or column_num > len(df.columns):
                print("Invalid column number. Please try again.")
            else:
                column_name = df.columns[column_num - 1]
                sort_order = input("Enter the sort order (A)scending or (D)escending: ")
            if sort_order.upper() == "A":
                sorted_df = df.sort_values(by=column_name, ascending=True)
                print(sorted_df)
            elif sort_order.upper() == "D":
                sorted_df = df.sort_values(by=column_name, ascending=False)
                print(sorted_df)
            else:
                print("Invalid sort order. Please try again.")

# ______________ (26) Print Specified Amount ______________

        elif action == "26":
            print("Choose 100, 1000, 5000 to print:")
            numprint = input(now.strftime("[%H:%M:%S]") + " ")
            if numprint == "100":
                print(df.head(n=100).to_string(index=False))
            if numprint == "1000":
                print(df.head(n=1000).to_string(index=False))
            if numprint == "5000":
                print(df.head(n=5000).to_string(index=False))

# __________________ (25) Quit MENU _____________________-
        
        elif action == "27":
            break
        else:
            print("\nInvalid option selected.")


def da3(df):
    from datetime import datetime
    import calendar
    q3 =df.nunique()
    
    from datetime import datetime
   
    # grouped_df = df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], format='%m/%d/%Y %H:%M:%S %p')

    #convert date into month format
    grouped_df =df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')

    grouped_df =df['year'] = df['DATE OCC'].dt.year
    grouped_df =df['month'] = df['DATE OCC'].dt.month_name()


    grouped_df = df.groupby(['month', 'Crm Cd Desc'])['Crm Cd Desc'].count().reset_index(name='unique_count')
    grouped_df = grouped_df.sort_values('unique_count', ascending=False)

    print(grouped_df)
    print("total unique count: ",len(grouped_df))



def da2(df):
    q2 =df.nunique()
    #sorting function if needed
    sorted_df = df.sort_values('AREA NAME')

    #group with area name
    grouped_df = df.groupby(['AREA NAME', 'year', 'Crm Cd Desc']).size().reset_index(name='top5')


    #sort values from area name above 
    top5an = grouped_df.sort_values(by=['top5'], ascending=False).head(5)

    print(top5an)

def da1(df):
    q1 =df.nunique()


    #df.dtypes
    df['year'] = df['year'].astype(int)
    sorted_df = df.sort_values('year')
    #grouped_df = df.groupby(['year', 'Crm Cd Desc'])['Crm Cd'].nunique()
    #sorted_df = grouped_df.sort_index()

    #uniquecount by crime descption, and ascend by year 
    grouped_df = df.groupby(['Crm Cd Desc','year'])['Crm Cd Desc'].nunique().reset_index(name='uniqueCount')

    # sort the DataFrame in descending order by the number of unique crimes
    sorted_df = grouped_df.sort_values('year', ascending=True)
    
    #df.sort_values(by="year")

    print(sorted_df)
    #print(sorted_df.to_frame().reset_index().rename(columns={'year': 'years'}))
    print("total unique count: ",len(sorted_df))
    

def dataAnalysis():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print(current_time,"Show the total unique count of crimes per year sorted in descending order")
    q1 =da1(df)
    print("********************")
    print("")
    print(current_time,"hot the top 5 areas (AREA NAME) with the mos crime events in all years (Sorted by the number of crime events)")
    q2 =da2(df)
    print("********************")
    print("")
    print(current_time,"Show all months and the unique total count of crimes sorted in increasing order.")
    q3 =da3(df)
    print("********************")
    print("")

# -------------------- Main Program Loop --------------------

while True:
    #______ Current time _______
    
    now = datetime.datetime.now()

    # ____________ User selects an option _________
    
    print(menu)
    action = input("Please select an option: ")

    # ______________ Load data from dataset _______
    
    if action == "1":
        load_data()

    # __________ Dataset isn't loaded __________
    
    elif action == "2":
        if df is None:
            print("\nPlease load a data set first!")
        else:
            explore_data()

    elif action == "3":
        if df is None:
            print("\nPlease load a data set first!")
        else:
            dataAnalysis()
    # __________ Print Data Set __________
    elif action == "4":
        if df is None:
            print("\nPlease load a data set first!")
        else:
            print(pd.DataFrame(df))
    # __________________ Quit Program _________
    
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