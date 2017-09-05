import time
t0 = time.clock()
print t0
for a in range(0,101):
    while a%2 ==0:
        print a
        break

print (time.clock()-t0)

