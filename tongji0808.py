count = 0
f = open("0808a.txt","r")
str1 =f.read().replace("\n",",")
list1 = str1.split(",")
for i in range(len(list1)):
    if(int(list1[i]) > 5):
        count=count+1
f.close()
print count



