'''

    install mysql.connector
    https://stackoverflow.com/questions/50243506/caching-sha2-password-is-not-supported-mysql?rq=1


    https://stackoverflow.com/questions/20463333/mysqldb-python-insert-d-and-s
    check 38 here

    https://stackoverflow.com/questions/5507948/how-can-i-insert-null-data-into-mysql-database-with-python
    check 172 here

    # pip install mysqlclient for MySQLdb
    -   encoidng is done o remove the junk value being appended
    https://stackoverflow.com/questions/46239288/remove-single-quote-from-list-in-python/46239380


    with open('EMPLOYEE.csv',encoding="utf-8-sig") as csv_file:
    file_csv = csv.reader(csv_file, delimiter=',',skipinitialspace=True)



    ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.
  csv_file = pd.read_csv(txt_file, delimiter=', ', header=None)
'''
'''
-- Specify to check foreign key constraints (this is the default)
    SET FOREIGN_KEY_CHECKS = 1;

   -- Do not check foreign key constraints
    SET FOREIGN_KEY_CHECKS = 0;

'''

import mysql.connector
import csv
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rathod@1996",
    database="COMPANY"
)
'''
        Before inserting the text file see if there is uneven space after comma
        if so replace  'comma space'  with 'comma'
        then 'comma' with 'comma space'

'''

# Take input as text file and convert it into csv.



# Ask the user in which table they wants to load the data they just provided



# Todo: this is Employee Table
# create a  csv file
txt_file = "EMPLOYEE.txt"
csv_file = pd.read_csv(txt_file, delimiter=', ', header=None, engine='python')
csv_file.to_csv('EMPLOYEE.csv', index=None, header=None, na_rep='null')

# open connection cursor and create foreign key constrain
mycursor = mydb.cursor()
mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")

# add values
val = []
# Open the csv file and read the value to insert it into database
with open('EMPLOYEE.csv', encoding="utf-8-sig") as csv_file:
    file_csv = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    for line in file_csv:
        row = []
        for i in range(len(line)):
            # removing extra quotes that get added when we add a string into a list
            row.append(line[i].strip('\''))
        # print(row)
        lst = []
        for i in range(len(row)):
            if row[i] == 'null':
                lst.append(None)
            else:
                lst.append(row[i])
        # print("\n\n")
        # print(lst)

        # load value into csv file
        try:
            sql = "INSERT INTO EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, lst)
            # mydb.commit()
        except mysql.connector.IntegrityError as err:
            # print("Error: {}".format(err))
            # print("Error encountered! Ignoring that line and continuing")
            continue
print("record were inserted.")
mydb.commit()



# Todo: this is DEPARTMENT Table
# create a  csv file
txt_file = "DEPARTMENT.txt"
csv_file = pd.read_csv(txt_file, delimiter=', ', header=None, engine='python')
csv_file.to_csv('DEPARTMENT.csv', index=None, header=None, na_rep='null')

# open connection cursor and create foreign key constrain
mycursor = mydb.cursor()
mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")

# add values
val = []
# Open the csv file and read the value to insert it into database
with open('DEPARTMENT.csv', encoding="utf-8-sig") as csv_file:
    file_csv = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    for line in file_csv:
        row = []
        for i in range(len(line)):
            # removing extra quotes that get added when we add a string into a list
            row.append(line[i].strip('\''))
        # print(row)
        lst = []
        for i in range(len(row)):
            if row[i] == 'null':
                lst.append(None)
            else:
                lst.append(row[i])
        # print("\n\n")
        # print(lst)

        # load value into csv file
        try:
            sql = "INSERT INTO DEPARTMENT (Dname, Dnumber, Mgr_ssn, Mgr_start_date) VALUES (%s, %s, %s, %s)"
            mycursor.execute(sql, lst)
            # mydb.commit()
        except mysql.connector.IntegrityError as err:
            # print("Error: {}".format(err))
            # print("Error encountered! Ignoring that line and continuing")
            continue
print("record were inserted.")
mydb.commit()


# Todo: this is DEPT_LOCATIONS Table
# create a  csv file
txt_file = "DEPT_LOCATIONS.txt"
csv_file = pd.read_csv(txt_file, delimiter=', ', header=None, engine='python')
csv_file.to_csv('DEPT_LOCATIONS.csv', index=None, header=None, na_rep='null')

# open connection cursor and create foreign key constrain
mycursor = mydb.cursor()
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")

# add values
val = []
# Open the csv file and read the value to insert it into database
with open('DEPT_LOCATIONS.csv', encoding="utf-8-sig") as csv_file:
    file_csv = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    for line in file_csv:
        row = []
        for i in range(len(line)):
            # removing extra quotes that get added when we add a string into a list
            row.append(line[i].strip('\''))
        # print(row)
        lst = []
        for i in range(len(row)):
            if row[i] == 'null':
                lst.append(None)
            else:
                lst.append(row[i])
        # print("\n\n")
        # print(lst)

        # load value into csv file
        try:
            sql = "INSERT INTO DEPT_LOCATIONS (Dnumber, Dlocation) VALUES (%s, %s)"
            mycursor.execute(sql, lst)
            # mydb.commit()
        except mysql.connector.IntegrityError as err:
            # print("Error: {}".format(err))
            # print("Error encountered! Ignoring that line and continuing")
            continue
print("record were inserted.")
mydb.commit()



# Todo: this is PROJECT Table
txt_file = "PROJECT.txt"
csv_file = pd.read_csv(txt_file, delimiter=', ', header=None, engine='python')
csv_file.to_csv('PROJECT.csv', index=None, header=None, na_rep='null')

# open connection cursor and create foreign key constrain
mycursor = mydb.cursor()
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")

# add values
val = []
# Open the csv file and read the value to insert it into database
with open('PROJECT.csv', encoding="utf-8-sig") as csv_file:
    file_csv = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    for line in file_csv:
        row = []
        for i in range(len(line)):
            # removing extra quotes that get added when we add a string into a list
            row.append(line[i].strip('\''))
        # print(row)
        lst = []
        for i in range(len(row)):
            if row[i] == 'null':
                lst.append(None)
            else:
                lst.append(row[i])
        # print("\n\n")
        # print(lst)

        # load value into csv file
        try:
            sql = "INSERT INTO PROJECT (Pname, Pnumber, Plocation, Dnum) VALUES (%s, %s, %s, %s)"
            mycursor.execute(sql, lst)
            # mydb.commit()
        except mysql.connector.IntegrityError as err:
            # print("Error: {}".format(err))
            # print("Error encountered! Ignoring that line and continuing")
            continue
print("record were inserted.")
mydb.commit()



# Todo: this is WORKS_ON Table
txt_file = "WORKS_ON.txt"
csv_file = pd.read_csv(txt_file, delimiter=', ', header=None, engine='python')

csv_file.to_csv('WORKS_ON.csv', index=None, header=None, na_rep='null')

# open connection cursor and create foreign key constrain
mycursor = mydb.cursor()
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")

# add values
val = []
# Open the csv file and read the value to insert it into database
with open('WORKS_ON.csv', encoding="utf-8-sig") as csv_file:
    file_csv = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    for line in file_csv:
        row = []
        for i in range(len(line)):
            # removing extra quotes that get added when we add a string into a list
            row.append(line[i].strip('\''))
        # print(row)
        lst = []
        for i in range(len(row)):
            if row[i] == 'null':
                lst.append(None)
            else:
                lst.append(row[i])
        # print("\n\n")
        # print(lst)

        # load value into csv file
        try:
            sql = "INSERT INTO WORKS_ON (Essn, Pno, Hours) VALUES (%s, %s, %s)"
            mycursor.execute(sql, lst)
            # mydb.commit()
        except mysql.connector.IntegrityError as err:
            # print("Error: {}".format(err))
            # print("Error encountered! Ignoring that line and continuing")
            continue
print("record were inserted.")
mydb.commit()



# Todo: this is DEPENDENT Table
txt_file = "DEPENDENT.txt"
csv_file = pd.read_csv(txt_file, delimiter=', ', header=None, engine='python')

csv_file.to_csv('DEPENDENT.csv', index=None, header=None, na_rep='null')

# open connection cursor and create foreign key constrain
mycursor = mydb.cursor()
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")

# add values
val = []
# Open the csv file and read the value to insert it into database
with open('DEPENDENT.csv', encoding="utf-8-sig") as csv_file:
    file_csv = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    for line in file_csv:
        row = []
        for i in range(len(line)):
            # removing extra quotes that get added when we add a string into a list
            row.append(line[i].strip('\''))
        # print(row)
        lst = []
        for i in range(len(row)):
            if row[i] == 'null':
                lst.append(None)
            else:
                lst.append(row[i])
        # print("\n\n")
        # print(lst)

        # load value into csv file
        try:
            sql = "INSERT INTO DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, lst)
            # mydb.commit()
        except mysql.connector.IntegrityError as err:
            # print("Error: {}".format(err))
            # print("Error encountered! Ignoring that line and continuing")
            continue
print("record were inserted.")
mydb.commit()

