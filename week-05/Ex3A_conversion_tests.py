# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

a = float(a)
b = int(b)

# c = int(c) gives an error because steven can't become an integer
# d = int(d) gives an error because Number can't become an integer

a = int(float(a)) 
cNumber = int(c[0:3])
dNumber = int(d[7:8])

print(a, type(a)) 
print(b, type(b))
print(c, type(c))
print(cNumber, type(cNumber))
print(dNumber, type(dNumber))

