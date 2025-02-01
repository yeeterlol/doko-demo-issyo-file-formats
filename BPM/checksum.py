def basic_hash(name):
    res = 0
    for ch in name:
        c = ord(ch)
        # force uppercase any characters
        # the assembly never lies ¯\_(ツ)_/¯
        if 'a' <= ch <= 'z':
            c -= 0x20 
        res = (res * 31 + c) & 0xffffffff
    return res 

def get_ks_sum(name, pos, items):
    checksum = csum(name)
    calc = (checksum - (checksum // pos) * pos)
    c = calc % items
    return c