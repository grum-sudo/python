#def net_price(list_price, discount=0, tax=0.05):
#    return list_price * (1 - discount) * (1 + tax)
# print(net_price(100))
# print(net_price(100, 0.1))
#print(net_price(100, 0.1, 0))


import time

def count(end, start=0):
    for x in range(start, end):
        print(x)
        time.sleep(1)
    print("done")

count(5, 1)