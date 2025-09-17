import csv
import csvfileread
import pandas as pd
import sys

def search_in_two_df(modelname_path,file_path):
    df_modelname=csvfileread.read_csv(modelname_path)
    df_file=csvfileread.read_csv(file_path)
    #get the certain col name (modelname or number)
    col_name="Number"
    df_modelname["colname"]=df_modelname["modelname"].isin(df_file["modelname"])

    #wirte back to csv
    csvfileread.write_df_back_to_csv(df_modelname,modelname_path)


def main():
    if len(sys.argv)<3:
        print("Usage: python script.py <modelname_path> <file_path>")
        return
    modelname_path=sys.argv[1]
    file_path=sys.argv[2]
    search_in_two_df(modelname_path,file_path)  
    
if __name__=="__main__":
    main()




