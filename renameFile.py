

import os

def changeName(fileDir):
    
    nameSetting = 1
    newNameJpeg = f"{(nameSetting) :03d}.jpg"
    location = fileDir
    dir_list = os.listdir(location)

    for filename in dir_list:
        name, ext = os.path.splitext(filename)\
        
        print(name, ext)

        
        if ext == ".jpg" or ext == ".jpeg":
            os.rename(filename, newNameJpeg)
            nameSetting += 1 # <-- bump up name from 1 to 2 to ... so on
            newNameJpeg = f"{(nameSetting) :03d}.jpg"
            
    
changeName( ) # <--- put file directory here