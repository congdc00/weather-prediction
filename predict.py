
import csv
import matplotlib.pyplot as plt

def get_data_csv(path):

    with open(path) as f:
        reader = csv.reader(f)
        count = -1
        for row in reader:
            temperature = (int(row[1])  - 32) // 1.8

                

            
def find_data(root_path):
    year = 2004
    sum = 0
    count = 0
    while year < 2022:
        for month in range(1,13):
            day = 0
            while day<31:
                day+=1
                if month < 10:
                    name_month = '0' + str(month)
                else:
                    name_month = str(month)
                if day<10:
                    name_day = '0' + str(day)
                else:
                    name_day = str(day) 
                path = root_path + str(year) + '/' + str(year) + '-' +name_month +'-'+ name_day + '.csv'
                try:
                    get_data_csv(path)
                    print(path)
                except:
                    break
        year+=1

if __name__ == "__main__":
    root_path = './data/HCMC/'
    result = find_data(root_path)