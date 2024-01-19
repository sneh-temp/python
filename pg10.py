try:
    fname=input("Enter a file name:")
    fhand=open("/root/python/"+fname,'+rw')
except:
    print("File does not exist")

for file in fhand:
    print(file.strip().upper())