try:
    fname=input("Enter a file name:")
    fhand=open("/root/python/"+fname)
except:
    print("File not found.")
    quit()

count=0

for line in fhand:
    if line.startswith("From "):
        line=line.rstrip()
        words=line.split()
        count=count+1
        print(words[1])

print("There were "+str(count)+" lines in the file with From as the first word")