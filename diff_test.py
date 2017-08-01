import os
while True:
    for i in range(1,2001):
        stri = str(i)
        file = stri + '.txt'
        py = open(file)
        print py.read()
