import math
def cmb(n,r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

if __name__=='__main__':
    rslt=cmb(5,2)
    print(rslt)
