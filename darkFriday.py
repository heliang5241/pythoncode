#coding:utf-8
def get(y,m):
    if((y%4==0 and y%100!=0) or (y%400==0)):
        i=1
    else:
        i=0
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        return 31
    elif m==2:
        if(i==1):
            return 29
        else:
            return 28
    return 30
# 输入n，限定范围.注意转化为int类型
n = int(input())
while n<0 or n>400:
    n = input()
a= [0 for i in range(7)]
week=6
for i in range(1900,1900+n):
    for j in range(1,13):
        a[week%7]+=1
        week+=get(i,j)
print(str(a[6])+" "+str(a[0]))
for i in range(1,6):
    print(str(a[i])+" ")