d=0
def func(d,m):
    if m==0:
        return True
    elif d>=len(A):
        return False
    else:
        rslt=func(d+1,m) or func(d+1,m-A[d])
    return rslt

if __name__=="__main__":
    '''
    ある数列Aに対して整数mが与えられたとき、
    数列Aの中の組み合わせ(足し算限定）で整数mを作ることができるか否かを判定する
    '''
    A=[1,5,6,3,4]
    m=11
    rslt=func(d,m)
    print(rslt)