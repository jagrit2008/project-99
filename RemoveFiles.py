import os
import shutil
time.time()
os.path.join()
 os.stat(path)
path=input("enter the name of the foler to be sorted")

list_of_files=os.listdir(path)

for file in list_of_files:
    name,ext = os.path.splitext(file)
