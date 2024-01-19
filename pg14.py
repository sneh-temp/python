try:
    fhand=open("/root/python/romeo.txt")
except:
    print("File not found")
    exit()

unqword=list()

for line in fhand:
    words=line.split()
    for word in words:
        if word not in unqword:
            unqword.append(word)

print(sorted(unqword))