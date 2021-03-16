'''
マージソートと挿入ソートの処理時間を比較する
'''

import random
import string
import time
import copy

def merge(data,left,right):
    mid = int( (left+right) / 2 )
    n1 = mid - left
    n2 = right - mid
    leftData = [ data[0][i+left] for i in range(n1) ]
    leftData_str = [ data[1][i+left] for i in range(n1) ]

    rightData = [ data[0][i+mid] for i in range(n2) ]
    rightData_str = [ data[1][i+mid] for i in range(n2) ]
    i = 0
    j = 0
    leftData.append(float("inf"))
    rightData.append(float("inf"))

    for k in range(left,right):
        if leftData[i] <= rightData[j]:
            data[0][k] = leftData[i]
            data[1][k] = leftData_str[i]
            i += 1
        else:
            data[0][k] = rightData[j]
            data[1][k] = rightData_str[j]
            j += 1
 
def mergeSort(data,left,right):
    if left + 1 < right:
        mid = int( (left+right) / 2 )
        mergeSort(data,left,mid)
        mergeSort(data,mid,right)
        merge(data,left,right)

def insertion_sort(data):
    '''
    挿入ソート
    '''
    sorted_list=[[],[]]
    sorted_list[0].append(data[0][0])
    sorted_list[1].append(data[1][0])

    for i in range(1,len(data[0])):
        temp=data[0][i]
        temp_str=data[1][i]
        for x in range(i):
            if temp<sorted_list[0][x]:
                sorted_list[0].insert(x,temp)
                sorted_list[1].insert(x,temp_str)
                break
            elif temp>=sorted_list[0][-1]:
                sorted_list[0].append(temp)
                sorted_list[1].append(temp_str)
                break
            else:
                continue
    return sorted_list
 
if __name__ == "__main__":
    # 昇順降順設定
    # 昇順なら0,降順なら1
    order=1


    # ランダムな数値とアルファベットの二次元配列を作成
    input_num=[]
    input_str=[]
    for i in range(10000):
        x=random.randint(1,1000)
        y=random.choice(string.ascii_uppercase)
        input_num.append(x)
        input_str.append(y)

    input_data=[]
    input_data.append(input_num)
    input_data.append(input_str)
    # print('入力データ')
    # print(input_data)

    
    # 挿入ソートで実行する
    data1=copy.deepcopy(input_data)
    t1 = time.time()
    output1=insertion_sort(data1)
    t2 = time.time()
    if order==1:
        output1[0].reverse()
        output1[1].reverse()
    # print('挿入ソート：出力データ')
    # print(rslt)
    elapsed_time = t2 -t1
    print('挿入ソートのProccess Timeは {} [s] です'.format(elapsed_time))

    # マージソートで実行する
    output2=copy.deepcopy(input_data)
    t1 = time.time()
    mergeSort(output2,0,len(output2[0]))
    if order==1:
        output2[0].reverse()
        output2[1].reverse()
    
    t2 = time.time()
    # print('マージソート：出力データ')
    # print(input_data)
    elapsed_time = t2 -t1
    print('マージソートのProccess Timeは {} [s] です'.format(elapsed_time))

    # 安定なソートか判断する
    if output1[1]==output2[1]:
        print('安定なソートです')
    else:
        print('不安定なソートです')


