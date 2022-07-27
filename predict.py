
import csv
from unittest import result
import matplotlib.pyplot as plt

def get_data_csv(path, time, type, choice):

    with open(path) as f:
        reader = csv.reader(f)
        count = -1
        for row in reader:
            if row[0] == time:
                count += 1

            if count == type:
                print(row)
                return row[choice]
                

            
def find_data(root_path,date, time, type):
    year = 2004
    sum = 0
    count = 0
    while year < 2022:
        path = root_path + str(year) + '/' + str(year) + '-' + date + '.csv'
        year+=1
        data_tmp = get_data_csv(path, time, type, choice = 1)
        if data_tmp is not None:
            count += 1
            sum += int(data_tmp)
    result = sum/count 
    result = (result - 32) // 1.8
    return result
    

if __name__ == "__main__":
    root_path = './data/HCMC/'
    date= '07-27'
    time = '10:00'
    type = 0
    result = find_data(root_path,date,time,type)
    print("Nhiệt độ ngày {} lúc {} là {} độ C".format('2022' + '-' + date, time, result))