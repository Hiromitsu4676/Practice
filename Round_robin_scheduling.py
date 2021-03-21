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

class Roundrobin():
    '''
    ラウンドロビンスケジューリング
    '''
    def __init__(self,tlist,quantum):
        self.tlist=tlist
        self.quantum=quantum
        self.Q=Queue()

    def process(self):
        for i in range(len(self.tlist)):
            self.Q.enqueue(self.tlist[i])
        
        print('タスクリスト',self.Q.queue)

        while not self.Q.is_empty():
            temp=self.Q.dequeue()
            # print(temp,'処理するやつ')

            temp_task=temp.split(',')
            ID=temp_task[0]
            pros_time=int(temp_task[1])

            if pros_time<self.quantum:
                print('process{},{}ms'.format(ID,pros_time))
            else:
                remain=pros_time-self.quantum
                print('process{},{}ms'.format(ID,self.quantum))
                remain='{},{}'.format(ID,remain)
                self.Q.enqueue(remain)

if __name__ == "__main__":

    '''
    各プロセスIDと処理時間を受け取り、ランドロビンスケジュールで処理するメインプログラム
    '''
    
    task_list=['1001,50','1002,30','1003,500','1004,10']
    Quant=200
    output=Roundrobin(task_list,Q)
    output.process()
