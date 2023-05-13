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

# initialize variables
df = None

# ------------------- define functions for menu options -----------------------------

def load_data():

    global df
    files = {
            "1": "Crime_Data_from_2017_to_2019.csv"
            }

    # _______________ Selecting which .csv file to open _______
    while True:
        file_num = input(file_options + "\nPlease select an option: ")
        if file_num in files:

            filename = ""

        if file_num == "1":
            filename = "Crime_Data_from_2017_to_2019.csv"
            break
        else:
            print("Invalid file number. Please try again.")

        """
    elif file_num == "2":
        filename = "Crime_Data_from_2020_to_2021.csv"
    elif file_num == "3":
        filename = "Test.csv"
"""
    # __________ File Read Time _________

    start_time = time.time()
    df = pd.read_csv(filename)
    end_time = time.time()

    df = df.drop(['Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street'],  axis='columns')
    newdf = pd.DataFrame(df)

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
            print(df)

#___________________ (22) Select a column to drop __________________

        elif action == "22":
            print(now.strftime("[%H:%M:%S]") + "\nSelect a column number to drop from the list:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            try:
                col_num = input(now.strftime("[%H:%M:%S]") + " ")
                col_name = df.columns[int(col_num)-1]
                df.drop(col_name, axis=1, inplace=True)
                print(now.strftime("[%H:%M:%S]") + f" Column [{col_num}] {col_name} dropped!")
            except (ValueError, IndexError):
                print(now.strftime("[%H:%M:%S]") + " Invalid input. Please enter a valid column number.")

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
            while True:
                try:
                    col_num = int(input(now.strftime("[%H:%M:%S]") + " "))
                    if col_num < 1 or col_num > len(df.columns):
                        print("Invalid column number. Please enter a number between 1 and", len(df.columns))
                    else:
                        break
                except ValueError:
                    print("Inavlid Input. Enter a valid column")
            print("Column " + str(col_num) + " stats: \n============")
            #if col_num > 0 and col_num <= len(df.columns):
            column_name = df.columns[col_num - 1]
            column_stats = df[column_name].describe()
            print(column_stats)
            #else:
             #   print("Invalid column number. Please try again.")
# ______________ (24) Search for Specific Element ____________________
        elif action == "24":
            print("\nSelect column number to search within:\n" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]) + "\n")
            try:
                col_num = int(input(now.strftime("[%H:%M:%S]") + " "))
                #col_num = int(col_num)
                if col_num > 0 and col_num <= len(df.columns):
                    start_time = time.time()
                    column_name = df.columns[col_num - 1]
                    search_query = input(now.strftime("\n[%H:%M:%S]") + " Enter the element(s) to search for (separate by commas for multiple values): ")
                    search_values = [value.strip() for value in search_query.split(",")]
                    search_results = df[df[column_name].isin(search_values)].index.tolist()
                    if len(search_results) > 0:
                        end_time = time.time()
                        print(now.strftime("\n[%H:%M:%S]") + f" Element found in rows: {search_results}")
                        print("Search was successful! time to search was {end_time-start_time:.2f} sec.")
                    else:
                        print(f"\nNo results found in column '{column_name}'.")
                else:
                    print(f"\nInvalid input: please enter a number between 1 and {len(df.columns)}.")
            except ValueError:
                print("\nInvalid input. Please input a number")



# ______ (25) Sort Columns in either Ascending or Descending ___________
        elif action == "25":
            print("Which column do you want to sort?" + "\n".join([f"[{i}] {col}" for i, col in enumerate(df.columns, start=1)]))
            while True:
                try:
                    column_num = int(input("Enter the column number: "))
                    if column_num < 1 or column_num > len(df.columns):
                        raise ValueError("Invalid column number!")
                    #print("Invalid column number. Please try again.")
                    else:
                        column_name = df.columns[column_num - 1]
                        sort_order = input("Enter the sort order (A)scending or (D)escending: ")
                        if sort_order.upper() not in ("A", "D"):
                            raise ValueError("Invalid sort order")
                        break
                except ValueError as e:
                    print(str(e))
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
            else:
                print("invalid number")

# __________________ (25) Quit MENU _____________________-

        elif action == "27":
            break
        else:
            print("\nInvalid option selected.")

# -------------------- Main Program Loop --------------------

def q1(df):
    df['year'] = pd.to_datetime(df['DATE OCC']).dt.year
    crimes_per_year = df.groupby('year')['Crm Cd Desc'].nunique().reset_index()
    crimes_per_year = crimes_per_year.sort_values('Crm Cd Desc', ascending=False)
    print("Show the total unique count of crimes per year sorted in descending order.")
    print(crimes_per_year)
    print("**********")
    print("")


def q2(df):
    filtered_df = df[['AREA NAME', 'DATE OCC']]
    crime_counts = filtered_df.groupby('AREA NAME').size()
    sorted_crime_counts = crime_counts.sort_values(ascending=False)
    top_5_areas = sorted_crime_counts.head(5)
    print("\nTop 5 areas with the most crime events:")
    print(top_5_areas)
    print("**********")
    print("")


def q3(df):
    df['Date Rptd'] = pd.to_datetime(df['Date Rptd'])
    unique_crime_counts = df.groupby(df['Date Rptd'].dt.to_period('M'))['Crm Cd'].nunique()
    sorted_counts = unique_crime_counts.sort_values(ascending=True)
    print("\nUnique count of crimes for all months (sorted in increasing order):")
    print(sorted_counts)
    print("**********")
    print("")


def q5(df):
    hollywood_df = df[df['AREA NAME'] == 'Hollywood'].copy()
    hollywood_df.loc[:, 'TIME OCC'] = hollywood_df['TIME OCC'].astype(str)
    hollywood_df.loc[:, 'Hour'] = hollywood_df['TIME OCC'].apply(lambda x: int(x[:2]) if x.isdigit() and len(x) >= 2 else -1)
    hollywood_df = hollywood_df[hollywood_df['Hour'] != -1]
    hourly_crime_counts = hollywood_df['Hour'].value_counts()
    sorted_counts = hourly_crime_counts.sort_values(ascending=False)
    top_5_dangerous_times = sorted_counts.head(5)
    print("\nTop 5 most dangerous times (in hours) to be in Hollywood:")
    for hour, count in top_5_dangerous_times.iteritems():
        print(f"Hour: {hour}, Total Crimes: {count}")
    print("**********")
    print("")


def q6(df):
    df['Date Rptd'] = pd.to_datetime(df['Date Rptd'])
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    df['Report Time Difference'] = (df['Date Rptd'] - df['DATE OCC']).dt.days
    max_time_diff = df['Report Time Difference'].max()
    longest_reported_crimes = df[df['Report Time Difference'] == max_time_diff]
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 1000)
    pd.options.display.float_format = "{:.2f}".format
    print("\nDetails of the crimes that took the longest time to be reported:\n")
    print(longest_reported_crimes)
    df.drop('Report Time Difference', axis=1, inplace=True)
    print("**********")
    print("")

    

def q7(df):
    #df = df.groupby(['year', 'Crm Cd Desc']).sum().reset_index()
    # # grouped_df = df('year','Crm Cd Desc').size().reset_index(name='Count')
    # # sorted_df = grouped_df.sort_values(by='Count', ascending=False)

    # Calculate the sum of each crime type TOTAL AMOUNT
    # crime_counts = df.groupby('year','Crm Cd Desc').size().reset_index(name='total_count')
    # top_crimes = crime_counts.sort_values(by='total_count', ascending=False).head(10)
    # print(top_crimes)

    crime_counts = df.groupby(['year', 'Crm Cd Desc']).size().reset_index(name='total_count')

    # Sort the crime counts in descending order and list the top 10 crimes for PER YEAR
    for year in df['year'].unique():
        print(f'Top 10 most common crime types for year {year}:')
        year_crime_counts = crime_counts[crime_counts['year'] == year].sort_values(by='total_count', ascending=False).head(10)
        print(year_crime_counts)
    print("**********")
    print("")


def q8(df):

    # df.index = pd.to_datetime(df.index)

    # la_df = df.loc[df['AREA NAME'] == 'LOS ANGELES']

    # filtered_df = la_df.between_time('11:00:00', '13:00:00')

    # counts_time_range = filtered_df['Vict Sex'].value_counts()
    # counts_total = la_df['Vict Sex'].value_counts()

    # Print the results
    # print("Occurrences during specified time range:")
    # print(counts_time_range)
    # print("Occurrences in entire LA DataFrame:")
    # print(counts_total)

    
    df.index = pd.to_datetime(df.index)

    filtered_df = df.between_time('11:00:00', '13:00:00')

    counts_time_range = filtered_df['Vict Sex'].value_counts()

    counts_total = df['Vict Sex'].value_counts()


    print("Occurrences during specified time range:")
    print(counts_time_range)
    print("Occurrences in entire DataFrame:")
    print(counts_total)
    print("Men are likely to be more of a victim")

    # filtered_df = df[df['Premis Desc'] == 'LA']

    # # Count the number of occurrences for each gender
    # counts = filtered_df['Vict Sex'].value_counts()

    # # Print the results
    # print(counts)

##def d9(df):
    #Insert code here

def q10(df):
    filtered_df = df[(df['Vict Age'] >= 65) & (df['Vict Sex'] == 'M') & (df['year'] == 2018)]
    grouped_df = filtered_df.groupby('Premis Desc').size().reset_index(name='Count')
    sorted_df = grouped_df.sort_values(by='Count', ascending=False)
    #print the top 5 dangerous areas for older men in December 2018
    print("List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018.")
    print(sorted_df.head(5))
    total_count = grouped_df['Count'].sum()
    print ("Total Count", total_count)
    print("**********")
    print("")

    print("This is question 10 result")


#missing questions 4, 8, 9
def dataAnalysis():
    #a8 = q8(df)
    #a9 = q9(df)
    #a10 = q10(df)
    while True: 
        try:
            an1 = q1(df)
        except (RuntimeError, TypeError, NameError, KeyError,ValueError):
            print("Error in q1 function. Please reload data to see this information")
            break

        try:
            an2 = q2(df)      
        except (RuntimeError, TypeError, NameError, KeyError,ValueError): 
            print("Error in q2 function. Please reload data to see this information")
            break
            
        try:
            an3 = q3(df)                
        except (RuntimeError, TypeError, NameError, KeyError,ValueError):
            print("Error in q3 function. Please reload data to see this information")
            break
                
        try:
            an4 = q5(df)                
        except (RuntimeError, TypeError, NameError, KeyError,ValueError): 
            print("Error in q5 function. Please reload data to see this information")
            break
            
        try:
            an5 = q6(df)               
        except (RuntimeError, TypeError, NameError, KeyError,ValueError): 
            print("Error in q6 function. Please reload data to see this information")
            break

        try:
            an7 = q7(df)               
        except (RuntimeError, TypeError, NameError, KeyError,ValueError): 
            print("Error in q7 function. Please reload data to see this information")
            break

        try:
            an8 = q8(df)               
        except (RuntimeError, TypeError, NameError, KeyError,ValueError): 
            print("Error in q8 function. Please reload data to see this information")
            break

        # try:
        #     an9 = q9(df)               
        # except (RuntimeError, TypeError, NameError, KeyError,ValueError): 
        #     print("Error in q8 function. Please reload data to see this information")
        #     break

        try:
            an10 = q10(df)
        except (RuntimeError, TypeError, NameError, KeyError,ValueError):
            print("Error in q10 function. Please reload data to see this information")
            break




        break
    
    print("Data analysis complete.")
            
   

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
    # __________ Print Data Set __________
    elif action == "3":
        if df is None:
            print("\nPlease load a data set first!")
        else:
            dataAnalysis()
        #--------------------------------------------------------------------------------------------------------------------------------------------
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