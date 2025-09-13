import os
import pandas as pd
import sys

#read csv to df
def read_csv(csv_path):
    if os.path.exists(csv_path):
        return  pd.read_csv(csv_path)
    else:
        print("file not found")
        return None

#get all the folder names
def get_folder_name(folder_path):
    if(os.path.exists(folder_path)):
        return os.listdir(folder_path) #list

#take off the RoHS
def shorten_modelname(df):
    df["short_modelname"]=df["modelname"].str.replace(r"-RoHS.*","",regex=True)

#mapping the modelname and the folder name
def mapping_folder_name(df_modelname,list_folder_name):
    for index, name in df_modelname["short_modelname"].items():
        df_modelname.loc[index,"??"]="X"
        for folder in list_folder_name:
            if name in folder:
                df_modelname.loc[index,"??"]="O"
                break

def write_df_back_to_csv(df,csv_path):
    with open (csv_path,"w") as f:
        df.to_csv(csv_path, index=False)

#open a csv file 
#write the model name and require files
#store 
def main():
    if len(sys.argv)<3:
        print("Usage: python script.py <csv_path> <folder_path>")
        return
    
    csv_path=sys.argv[1]
    df=read_csv(csv_path)
    if df is None:
        return
    folder_path=sys.argv[2]
    l=get_folder_name(folder_path)
    #shorten_modelname(df) can be done in excel first
    mapping_folder_name(df,l)
    write_df_back_to_csv(df,csv_path)


if __name__=="__main__":
    main()