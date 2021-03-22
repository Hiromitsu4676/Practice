import dataclasses
import random
import string
import time
import copy


@dataclasses.dataclass
class Data:
    val: int
    alp: str

def insertion_sort(data):
    sorted_list=[]
    sorted_list.append(data[0])

    for i in range(1,len(data)):
        temp=data[i].val
        for x in range(i):
            if temp<sorted_list[x].val:
                sorted_list.insert(x,data[i])
                break
            elif temp>=sorted_list[-1].val:
                sorted_list.append(data[i])
                break
            else:
                continue
    print(sorted_list)
    return sorted_list


def counting_sort(data):
    C=[0]*(maxVal+1)
    for i in range(len(data)):
        index=data[i].val
        C[index] +=1

    count=0
    for i in range(len(C)):
        if C[i]>0:
            count +=C[i]
            C[i]=count
    
    sorted_list=[None]*len(data)

    for i in range(len(data)):
        temp_val=data[i].val
        temp_index=C[temp_val]
        sorted_list[temp_index-1]=data[i]
        C[temp_val] -=1
    return sorted_list

if __name__=='__main__':
    input_data=[]
    n=1000
    maxVal=100
    for i in range(n):
        x=random.randint(0,maxVal)
        y=random.choice(string.ascii_uppercase)
        temp=Data(x,y)
        input_data.append(temp)
    # print(input_data)

    # 挿入ソートで実行する
    data1=copy.deepcopy(input_data)
    t1 = time.time()
    output1=insertion_sort(data1)
    t2 = time.time()
    prpcess_time1 = t2 -t1

    #カウンティングソートで実行する   
    data2=copy.deepcopy(input_data)
    t1 = time.time()
    output2=counting_sort(data2)
    t2 = time.time()
    prpcess_time2 = t2 -t1

     # 処理時間表示
    print('挿入ソートのProccess Timeは {} [s] です'.format(prpcess_time1))
    print('カウンティンソートのProccess Timeは {} [s] です'.format(prpcess_time2))

    # 安定なソートか判断する
    if output1==output2:
        print('安定なソートです')
    else:
        print('不安定なソートです')


