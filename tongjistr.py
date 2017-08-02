
str ='''Error response from daemon: conflict: unable to remove repository reference "ubuntu" (must force) - container 40d59b73842b is using its referenced image 14f60031763d'''
mylist = list(str)
myset = set(mylist)
# print mylist
# print myset
max = 0
# print fcflist
for item in myset:
    print(item, mylist.count(item))
    if(max < mylist.count(item)):
        max = mylist.count(item)
print max

