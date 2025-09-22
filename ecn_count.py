#4 files count the number of exist

import csv
import csvfileread
import pandas as pd
import sys
import os

#for ECN count
#phase should be count too
def count(df_modelname,df_file,col_name):
    counts = df_file["??"].value_counts()
    df_modelname[col_name] = df_modelname["modelname"].map(counts).fillna(0).astype(int)
    return df_modelname

def main():
    if len(sys.argv)<3:
        print("Usage: python script.py <modelname_path> <file_dir>")
        return
    modelname_path=sys.argv[1]
    file_dir=sys.argv[2]
    df_modelname=csvfileread.read_csv(modelname_path)
    for file in os.listdir(file_dir):
        file_path=os.path.join(file_dir,file)
        df_file=csvfileread.read_csv(file_path)
        df_modelname=count(df_modelname,df_file,file)
    #write back to csv
    with open(modelname_path,"w") as f:
        df_modelname.to_csv(modelname_path, index=False)


if __name__=="__main__":
    main()