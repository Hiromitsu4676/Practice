import heapq

def get_adjacant_matlix(data,n):
    adjacent_matrix=[[] for _ in range(n)]
    for i in range(n):
        temp=[-1]*n
        k=data[i][1]
        for j in range(k):
            index=data[i][2*j+2]
            w=data[i][2*j+3]
            temp[index]=w
        adjacent_matrix[i]=temp

    return adjacent_matrix

def dijkstra(M,s):
    n=len(M)
    color=['White']*n
    d=[float('inf')]*n

    d[s]=0
    PQ=[(s,0)]
    heapq.heapify(PQ)

    while len(PQ)>0:
        mincost,u=heapq.heappop(PQ)

        color[u]='Black'

        for i,v in enumerate(M[u]):
            if i%2==0:
                if color[v]==2:
                    continue
                if d[u]+M[u][i+1]<d[v]:
                    d[v]=d[u]+M[u][i+1]
                    color[v]='Gray'
                    heapq.heappush(PQ,(d[v],v))
    return d

if __name__=='__main__':

    input_data=[]
    input_data.append('5')
    input_data.append('0 3 2 3 3 1 1 2')
    input_data.append('1 2 0 2 3 4')
    input_data.append('2 3 0 3 3 1 4 1')
    input_data.append('3 4 2 1 0 1 1 4 4 3')
    input_data.append('4 2 2 1 3 3')

    N=int(input_data.pop(0))


    adjacent_list = [ [] for i in range(N) ]
    for i in range(N):
        adjacent_list[i]=list(map(int,input_data.pop(0).split()))

    M=get_adjacant_matlix(adjacent_list,N)
    
    s=0

    rslt=dijkstra(M,s)
    for j in range(len(rslt)):
        print(j,rslt[j])

