import os
from csvfileread import read_csv
import sys
#list out all the file in the folder
#use os.walk
#find out the parent folder that inside it has only empty folders or empty files
def get_empty_parent_folder(root_path):
    result=[]
    for root,dirs,files in os.walk(root_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if not files and not dirs:
            True
        elif not files and dirs:
            all_empty=True
            for dir in dirs:
                dir_path=os.path.join(root, dir)
                if os.listdir(dir_path):
                    all_empty=False
                    break
            if all_empty:
                print(os.path.relpath(root,root_path), "folder with only empty folders")
                result.append(os.path.relpath(root, root_path))
    return result

#write function that use set to store the result. result should be seperate by os.sep and only keep the first and second words separated by os.sep
#for example, if the result is folder1/folder2/folder3, only keep folder1/folder2
def get_empty_parent_folder_v2(result):
    s=set()
    for path in result:
        parts=path.split(os.sep)
        if len(parts)>=2:
            s.add(os.sep.join(parts[:2]))
        elif len(parts)==1:
            s.add(parts[0])
    return s

#based on the set the split(os.sep)[0] and [1] will be the column and row name that i will lookup in other file 
def record_to_scv(s,csv_path):
    df=read_csv(csv_path)
    if df is None:
        return
    
    for path in s:
        parts=path.split(os.sep)
        if len(parts)>=2:
            modelname=parts[0]
            required_filename=parts[1]
            df.loc[df["modelname"]==modelname, "required_filename"]="X"

    df.to_csv(csv_path, index=False)

def main():
    if len(sys.argv)<=2:
        print("Usage: python script.py <root_path><csv_path>")
        return
    root_path=sys.argv[1]
    csv_path=sys.argv[2]
    result=get_empty_parent_folder(root_path)
    s=get_empty_parent_folder_v2(result)
    print("_______________________________________-")
    print(s)
    record_to_scv(s,csv_path)

if __name__=="__main__":
    main()