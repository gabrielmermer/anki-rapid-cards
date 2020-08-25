import csv
import os
from datetime import datetime
from pathlib import Path

os.system('cls' if os.name == 'nt' else 'clear')

# file name generation

filename = ""

name_validation_gate = 0 

def nameTheFile():

    global filename
    global name_validation_gate 

    filename = ""

    today_date = datetime.today().strftime('%Y-%m-%d')

    filename = input("insert the file name: ")

    filename = "--" + filename

    filename = today_date + filename

    # filename validation
    if os.path.exists(filename + ".csv"):
        print("file name in use, please choose diferent file name")
        return False
    else:   
        name_validation_gate = 1
        return True


while name_validation_gate == 0:
    nameTheFile()
        

# filename validation
print(filename)


tag = input("insert tag name (or press enter for empty): ")

print("to exit the script at any time please press . and enter")


card_count = 1
while True:

    os.system('cls' if os.name == 'nt' else 'clear')
    card_list = []

    print(card_count,'',end='')
    front_side = str(input("> "))
    if front_side == ".":
        break

    os.system('cls' if os.name == 'nt' else 'clear')

    back_side = str(input(">> "))

    os.system('cls' if os.name == 'nt' else 'clear')

    card_list.append(front_side)
    card_list.append(back_side)
    card_list.append(tag)

    current_row = [front_side,back_side,tag]

    table = open(filename + ".csv", 'a',encoding="utf-8")
    print("file open")
    tablewriter = csv.writer(table, delimiter='|')
    tablewriter.writerow(current_row)
    table.close()


    card_count +=1

#with open('/home/zubrzysta/Sync/school/output.csv', 'a') as table:
#    tablewriter = csv.writer(table, delimiter=';')
#    for i in master_list:
#        tablewriter.writerow(i)

