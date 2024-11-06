

import os
import shutil

from_dir = "C:/Users/akash.patwa/Downloads/Ranjana information/path1"
to_dir ="C:/Users/akash.patwa/Downloads/Ranjana information/path3"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension=="":
       continue
    if extension in ['.gif','.png','.jpg','.JPEG']:
        path1= from_dir+ "/"+file_name
        path2= to_dir+"/"+"imagefiles"
        path3= to_dir+"/"+"imagefiles"+"/"+file_name
     
     
        if os.path.exists(path2):
           print("moving"+file_name+ "...")

           shutil.move(path1,path3)
        else:
           os.mkdir(path2)
           print("moving"+file_name+ "...")
        
           shutil.move(path1,path3)
        
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    

    if extension=="":
       continue
    if extension in ['.py','.pyc','.pyo']:
        path1= from_dir+ "/"+file_name
        path2= to_dir+"/"+"python files"
        path3= to_dir+"/"+"python files"+"/"+file_name
     
     
        if os.path.exists(path2):
          print("moving"+file_name+ "...")

          shutil.move(path1,path3)
        else:
           os.mkdir(path2)
           print("moving"+file_name+ "...")
        
           shutil.move(path1,path3)   

        
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)

    if extension=="":
       continue
    if extension in ['.pdf','.doc','.txt','.ppt']:
        path1= from_dir+ "/"+file_name
        path2= to_dir+"/"+"Document"
        path3= to_dir+"/"+"Document"+"/"+file_name
     
     
        if os.path.exists(path2):
            print("moving"+file_name+ "...")

            shutil.move(path1,path3)
        else:
             os.mkdir(path2)
             print("moving"+file_name+ "...")
        
        shutil.move(path1,path3)   
             