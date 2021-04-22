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

def bfs_check(alist,start,end):

    color=['White']*len(alist)

    Q=Queue()
    Q.enqueue(start)
    while Q.is_empty()!=True:
        u = Q.dequeue()
        color[u] = 'Black'
        for n in alist[u]:
            if color[n]=='White':
                Q.enqueue(n)
            if n == end:
                return True
    return False


if __name__=='__main__':
    
    input_data=[]
    input_data.append('10 9')
    input_data.append('0 1')
    input_data.append('0 2')
    input_data.append('3 4')
    input_data.append('5 7')
    input_data.append('5 6')
    input_data.append('6 7')
    input_data.append('6 8')
    input_data.append('7 8')
    input_data.append('8 9')
    input_data.append('3')
    input_data.append('0 1')
    input_data.append('5 9')
    input_data.append('1 3')

    N,E=map(int,input_data.pop(0).split())
    
    adjacent_list=[[] for i in range(E)]

    for i in range(E):
        u,v = map(int,input_data.pop(0).split())
        adjacent_list[u].append(v)

    q_number=int(input_data.pop(0))

    for j in range(q_number):
        start,end=map(int,input_data.pop(0).split())
        rslt=bfs_check(adjacent_list,start,end)

        if rslt==True:
            print('Yes')
        else:
            print('No')


    
