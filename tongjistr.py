str ='''Error response from daemon: conflict: unable to remove repository reference "ubuntu" (must force) - container 40d59b73842b is using its referenced image 14f60031763d'''
oldlist = list(str)
newlist = set(oldlist)
max = 0
str = ''
for item in newlist:
    print(item, oldlist.count(item))
    if(max < oldlist.count(item)):
        max = oldlist.count(item)
print max

