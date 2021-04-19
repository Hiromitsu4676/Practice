def get_adjacant_matlix(data,n):
    adjacent_matrix=[[]]
    for i in range(n):
        temp=[0]*n
        k=adjacent_list[i][1]
        for j in range(k):
            index=adjacent_list[i][j+2]
            temp[index-1]=1
        adjacent_matrix.append(temp)

    del adjacent_matrix[0]

    return adjacent_matrix

class Queue():
    '''
    キュー（先入れ先出し）
    '''
    def __init__(self,size=100):
        self.queue =[]
        self.size=size
    def enqueue(self,x):
        self.queue.append(x)
        return self.queue
    def dequeue(self):
        rslt=self.queue[0]
        del self.queue[0]
        return rslt 
    def is_empty(self):
        return len(self.queue)==0

if __name__=='__main__':

    input_data=[]
    input_data.append('4')
    input_data.append('1 2 2 4')
    input_data.append('2 1 4')
    input_data.append('3 0')
    input_data.append('4 1 3')

    N=int(input_data.pop(0))


    adjacent_list=[[]]
    for i in range(N):
        temp=input_data.pop(0)
        temp=list(map(int,temp.split()))
        adjacent_list.append(temp)
    del adjacent_list[0]

    M=get_adjacant_matlix(adjacent_list,N)
    
    
    color=['White']*N
    d=[None]*N
    Q=Queue()

    s=0

    color[s]='Gray'
    d[s]=0
    Q.enqueue(s)
    
    while Q.is_empty()!=True:
        u=Q.dequeue()
        for k in range(N):
            if M[u][k]==1 and color[k]=='White':
                color[k]='Gray'
                d[k]=d[u]+1
                Q.enqueue(k)
        color[u]='Black'
    
    for j in range(N):
        print(j+1,d[j])




