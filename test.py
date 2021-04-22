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

    q_number=input_data.pop(0)

    # for k in range(q_number):
    #     q_input=list(map(int,input_data.pop(0).split()))

    
    color=['white']*N
    Q=Queue()

    s=0
    Q.enqueue(s)
    
    while Q.is_empty()!=True:
        u=Q.dequeue()
        color[s]='Gray'
        for k in range(N):
            if adjacent_list[k]=='White':

    
    
