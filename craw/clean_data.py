
import csv
import glob
import os
YEAR = '2021'
def read_csv(path):

    with open(path) as f:
        reader = csv.reader(f)
        new_csv = []
        for row in reader:
            new_line = []

            for sentence in row:
                list_word = sentence.split()
                new_line.append(list_word[0])

            new_csv.append(new_line)
    return new_csv

def get_new_path(old_path):
    root_path = "../data/HCMC/"+YEAR +'/'
    tmp = old_path.split("HCMC")
    name = root_path+ tmp[-1] 
    return name

def write_csv(path, new_csv):
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f) 
        for line in new_csv:
            writer.writerow(line)

def extract_name(path):

    list_info = path.split("/")
    len_name = len(list_info) - 1
    name = list_info[len_name]

    return name

def get_all_path(root_path):

    '''
    Load toàn bộ dữ liệu từ các file csv
    input: root_path file chứa data
    output: list path
    '''

    # Tìm tất cả các path csv
    list_path = glob.glob(os.path.join(root_path, "*.csv"))

    return list_path

def process(path):
    list_path = get_all_path(path)
    for path in list_path:
        new_csv = read_csv(path)
        new_path = get_new_path(path)
        write_csv(new_path, new_csv)

if __name__ == "__main__":
    path = '../data/HCMC/HCMC' + YEAR
    process(path)
    
