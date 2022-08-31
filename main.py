
#fnmatch module is used for file searching for with respect of extensions 

import os 
import fnmatch
import shutil

# your_path=input('Type your path to search documents?------>')

# os.chdir(os.path.join(os.getcwd(),"file_filter"))

# print(os.getcwd())

os.chdir(r"C:\Users\ghosh\Downloads")


img_destination=os.path.join(os.getcwd(),"all_folder","photo")
doc_destination=os.path.join(os.getcwd(),"all_folder","documents")




 #This function find out  below mentioned image extension  from pre defined 
 #folders for this purpose  you can change your searching place        
def image_finder():
    file_found=0
    img_lis=['*.png','*.jpg','*.jpeg']
    for file in os.listdir(os.getcwd()):
        for ext in img_lis:
            if fnmatch.fnmatch(file,ext):
                file_found+=1
                shutil.copy(os.path.join(os.getcwd(),file),img_destination)
            
    if file_found!=0:
        print(f"{file_found} nos file found")
    else:
        print("No file is found")
            
    

def doc_finder():
    file_found=0
    doc_lis=['*.pdf','*.docx','*.xlsx']
    for file in os.listdir(os.getcwd()):
        for ext in doc_lis:
            if fnmatch.fnmatch(file,ext):
                file_found+=1
                shutil.copy(os.path.join(os.getcwd(),file),doc_destination)
            
    if file_found!=0:
        print(f"{file_found} nos file found")
    else:
        print("No file is found")



if __name__=="__main__":
    image_finder()
    doc_finder()