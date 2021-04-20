class Stack():
    def __init__(self,size=100):
        self.stack=[]*size
        self.size=size
    def push(self,x):
        self.stack.append(x)
        return self.stack
    def pop(self):
        rslt=self.stack[-1]
        del self.stack[-1]
        return rslt
    def is_empty(self):
        return len(self.stack)==0

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

if __name__=='__main__':

    input_data=[]
    input_data.append('6')
    input_data.append('1 2 2 3')
    input_data.append('2 2 3 4')
    input_data.append('3 1 5')
    input_data.append('4 1 6')
    input_data.append('5 1 6')
    input_data.append('6 0')

    N=int(input_data.pop(0))

    adjacent_list=[[]]
    for i in range(N):
        temp=input_data.pop(0)
        temp=list(map(int,temp.split()))
        adjacent_list.append(temp)
    del adjacent_list[0]

    M=get_adjacant_matlix(adjacent_list,N)


    color=['White']*N
    time=1
    S=Stack()
    discover_time=[0]*N
    finish_time=[0]*N
    
    s=0
    # スタックに最初のノードを入れる
    S.push(s)
    # 探索中ラベルをつける
    color[s]='Gray'
    # ノード発見時刻を入れる
    discover_time[s]=time

    while S.is_empty()!=True:
        # スタックの一番上の要素を該当ノードとして参照する
        u=S.stack[-1]

        count=0
        for j in range(N):
            if M[u][j]==1 and color[j]=='White':
                color[j]='Gray'
                S.push(j)
                time +=1
                discover_time[j]=time
                count+=1
        
        if count==0:
            temp=S.pop()
            time +=1
            finish_time[temp]=time
            color[temp]='Black'


    # rslt
    for i in range(N):
        print(i+1,discover_time[i],finish_time[i])
