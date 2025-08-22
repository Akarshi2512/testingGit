
def multi(*args):
    res = 1
    for i in args:
        res = res*i
    print(res)

multi(2,3)
multi(1,2,3,4,5)