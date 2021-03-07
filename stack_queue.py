'''
スタックとキューを格納する
'''

class Stack():
    '''
    スタック（先入れ後だし）
    '''
    def __init__(self,size=10):
        self.stack=[]*size
        self.size=size
    def push(self,x):
        if len(self.stack)==self.size:
            pass
        else:
            self.stack.append(x)
        return self.stack
    def pop(self):
        rslt=self.stack[-1]
        del self.stack[-1]
        return rslt
    def is_empty(self):
        return len(self.stack)==0
         

class Queue():
    '''
    キュー（先入れ先出し）
    '''
    def __init__(self,size=10):
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

if __name__ == "__main__":
    '''
    数値を標準入力で連続で受け取り、スタックとキューに格納するメインプログラム
    '''
    print("start input data. if you completed input, you type \"end\".")

    input_data = []
    while(1):
        tmp = input()
        if tmp == "end":
            break
        else:
            input_data.append(int(tmp))
    
    ST=Stack(10)
    Q=Queue(10)

    for i in range(len(input_data)):
        ST.push(input_data[i]) 
        Q.enqueue(input_data[i]) 


    print(ST.stack)
    print(Q.queue)
