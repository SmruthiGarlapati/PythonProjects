import os

os.chdir("..")
directory = input("Directory path: ")
print(directory)
os.chdir(directory)
dirList = os.listdir()
print(dirList)
count = 0
for x in dirList:
  count +=1

print(count)