try:
    fhand=open("/root/python/mbox-short.txt")
except:
    print("File doesn't exist")
    quit()

for line in fhand:
    line.strip()
    if line.startswith("From "):
        tarlin=line.split(' ')
        print(tarlin[2])