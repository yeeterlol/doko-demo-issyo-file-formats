def bkdr(name):
    res = 0
    for ch in name:
        c = ord(ch)
        # force uppercase any characters
        if 'a' <= ch <= 'z':
            c -= 0x20 
        res = (res * 31 + c) & 0xffffffff
    return res 

def packman_sum(name, items):
    hash = bkdr(name)
    res = hash % items
    print("hash -> ", res)
    print("offset -> ", ((res+1) * 16))
    return res
