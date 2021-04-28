def prim(M):
    n=len(M)
    
    color=['White']*n
    d=[float('inf')]*n
    p=[None]*n

    d[0]=0
    p[0]=-1

    while(1):
        mincost=float('inf')
        for i in range(n):
            if color[i]!='Black' and d[i]<mincost:
                mincost=d[i]
                u=i
        
        if mincost ==float('inf'):
            break
        
        color[u]='Black'

        for v in range(n):
            if color[v] !='Black' and M[u][v] !=-1:
                if M[u][v]<d[v]:
                    d[v]=M[u][v]
                    p[v]=u
                    color[v]='Gray'
    return d

if __name__=="__main__":

    input_data=[]

    input_data.append("5")
    input_data.append("-1 2 3 1 -1")
    input_data.append("2 -1 -1 4 -1")
    input_data.append("3 -1 -1 1 1")
    input_data.append("1 4 1 -1 3")
    input_data.append("-1 -1 1 3 -1")

    N = int(input_data.pop(0))

    m = [ list(map(int,input_data.pop(0).split())) for i in range(N) ]

    rslt=prim(m)
    print(sum(rslt))
