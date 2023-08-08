import os

os.chdir("..")
directory = input("Directory path: ")
print(directory)
os.chdir(directory)
dirList = os.listdir()
fileCount = 0
dirCount = 0
for x in dirList:
  if(os.path.isfile(x)):
    print(x + " File")
    fileCount +=1
  else:
    print(x + " Directory")
    dirCount +=1
    
    

print("File Count: " + str(fileCount))
print("Directory Count: " + str(dirCount))
#next step: list files/dir into a new file
