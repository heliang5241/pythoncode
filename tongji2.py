str ='''Error response from daemon: conflict: unable to remove repository reference "ubuntu" (must force) - container 40d59b73842b is using its referenced image 14f60031763d'''
list = list(str)
# print list
a = {}
for i in list:
    if list.count(i) > 1:
        a[i] = list.count(i)
print (a)
