

import binascii

def order_list():
    a = 'aa0902630000bb'
    a_list = []
    for i in a.split():
        a_list.append(binascii.a2b_hex(i))
    return a_list;


print order_list()
