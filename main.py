import pandas as pd 

if __name__ == "__main__":
    data = pd.read_csv("./craw_data/ao_ba_lo_nam.csv", sep = '/t', name = ['stars','content'])
    print(data.head)