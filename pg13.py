letters=['a','b','c','d']

def chop(letters):
    del letters[0]
    del letters[len(letters)-1]

def middle(letters):
    return letters[1:len(letters)-1]

# chop(letters)
letters=middle(letters)
print(letters)