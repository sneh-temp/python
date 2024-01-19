headers=["From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008","From stephen.marquard@mail.com Sat Jan 5 09:14:16 2008","From sneh@google.com Sat Jan 5 09:14:16 2008"]

# Extract uct.ac.za here

for header in headers:
    atpos=header.find('@')
    lastpos=header.find(' ',atpos)
    print(header[atpos+1:lastpos])