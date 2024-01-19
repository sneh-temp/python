try:
    fname=input("Enter a file name:")
    fhand=open("/root/python/"+fname)
except:
    print("File does not exist.")
    quit()

count=0
total=0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        pos=line.find(':')
        num=float(line[pos+1:])
        count=count+1
        total=total+num

print("Average spam confidence:",total/count)
