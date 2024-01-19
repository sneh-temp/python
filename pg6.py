total=0
count=0
curmax=None
curmin=None

def max(curmax,num):
    if curmax is None or num > curmax:
        return num
    else:
        return curmax

def min(curmin,num):
    if curmin is None or num < curmin:
        return num
    else:
        return curmin

while True:
    try:
        inp=input("> ")
        if inp=="done":
            break
        else:
            num=float(inp)
            count+=1
            total+=num
            curmax=max(curmax,num)
            curmin=min(curmin,num)
    except:
        print("Invalid input. Please enter a number.")

print("Total:", total)
print("Count: ",count)
print("Average: ",total/count)
print("Maximum number",curmax)
print("Minimum number",curmin)