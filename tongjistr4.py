import string
def get_max_value(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
if __name__ == '__main__':
    str = '''Error response from daemon: conflict: unable to remove repository reference "ubuntu" (must force) - container 40d59b73842b is using its referenced image 14f60031763d'''
    print get_max_value(str)