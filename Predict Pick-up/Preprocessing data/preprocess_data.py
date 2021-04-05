import csv
import copy
import datetime
import sys
import statistics

class Date:
    def __init__(self,date,month,year,hr):
        self.__date = datetime.datetime(year,month,date,hr)
    def nextHr(self):
        self.date += datetime.timedelta(hours=1)
    def getDate(self):
        return self.__date.strftime("%d/%m/%Y")
    def getHr(self):
        return self.__date.strftime("%H")

group = ["A_grid_Group","B_grid_Group","C_grid_Group","D_grid_Group"]

for file in group:
    #-------------------fix missing values---------------------
    fileName = file
    final = []
    skip_head = True
    start = 9
    start_date = Date(date=15,month=7,year=2019,hr=0)
    print("  start fix mmissing values...")
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            end = len(row)-1
            if skip_head == True:
                final.append(row)
                skip_head = False
            else:
                row_copy = copy.deepcopy(row)

                if row_copy[0] == start_date.getDate and row_copy[1] == start_date.getHr:

                    final.append(row_copy)
                    start_date.nextHr

                else:
                    some = copy.deepcopy(row)
                    for a in range(start,end+1):
                        some[a] = "0"

                    while row_copy[0] != start_date.getDate or row_copy[1] != start_date.getHr:
                        some[0] = start_date.getDate
                        some[1] = start_date.getHr
                        final.append(copy.deepcopy(some))
                        start_date.nextHr
                    
    fileName = fileName.split('.')[0] + "_fixed_missing_values.csv"
    with open(fileName,'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(final)
    print("    complete fix missing values.")

    #----------------------check missing values-----------------

    skip_head = True
    start_date = Date(date=15,month=7,year=2019,hr=0)
    print("start check missing values...")
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if skip_head == True:
                skip_head = False
            else:
                if row[0] != start_date.getDate or row[1] != start_date.getHr:
                    print("    missing!!!")
                    print(f"    missing in row : {{row}}")
                    sys.exit()
    print("    perfect!!!")

    #------------------------normalization-----------------

    skip_head = True
    ar = []
    final = []
    print("  start normalizaion...")
    #find sd and mean
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            end = len(row)-1
            if skip_head == True:
                skip_head = False
            else:
                for index in range(start,end+1):
                    ar.append(float(row[index]))

    sd = statistics.stdev(ar)
    mean = sum(ar) / len(ar)
    skip_head = True
    print(f"    ...{fileName}...")
    print(f"    sd : {sd}")
    print(f"    mean : {mean}")
    #normalization
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if skip_head == True:
                skip_head = False
                final.append(row)
            else:
                temp = copy.deepcopy(row)
                temp[1] = "{:.5f}".format((float(temp[1])/23)*(0.8)+0.1) # min-max normalization
                for index in range(start,end+1):
                    temp[index] = "{:.5f}".format((float(temp[index])-mean)/sd) # standardization normalization
                final.append(temp)

    with open(fileName.split('.')[0]+'_and_normalization.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(final)

    txt = open(fileName[0:12]+'_normalization_sd_and_mean.txt',"w+")
    txt.write(fileName[0:12]+"\n")
    txt.write(f"mean = {mean}\n")
    txt.write(f"sd = {sd}\n")
    txt.write("\n")
    txt.write("\n")
    txt.close

    print("    complete.\n")
