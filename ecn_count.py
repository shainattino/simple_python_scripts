#4 files count the number of exist

import csv
import csvfileread
import pandas as pd
import sys
import os

#for ECN count
#phase should be count too
def count(modelname_path,file_path):
    df_modelname=csvfileread.read_csv(modelname_path)
    df_file=csvfileread.read_csv(file_path)
    directory, file=os.path.split(file_path)
    col_name=file
    counts = df_file["??"].value_counts()
    df_modelname[col_name] = df_modelname["modelname"].map(counts).fillna(0).astype(int)
    #wirte back to csv
    with open(modelname_path,"w") as f:
        df_modelname.to_csv(modelname_path, index=False)

def main():
    if len(sys.argv)<3:
        print("Usage: python script.py <modelname_path> <file_path>")
        return
    modelname_path=sys.argv[1]
    file_path=sys.argv[2]
    count(modelname_path,file_path)


if __name__=="__main__":
    main()