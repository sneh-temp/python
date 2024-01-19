fruit = 'banana'

def count(string,target):
    counter=0
    for char in string:
        if char==target:
            counter=counter+1
    print("Character",r"'",target,r"'","occurs",counter,"times.")
    
count(fruit,'a')

print(fruit.count('a'))