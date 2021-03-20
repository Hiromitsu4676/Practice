import random
import string
import time
import copy

def partition(data,p,r):
    x = data[0][r]
    i = p - 1
    for j in range(p,r):
        if data[0][j] >= x:
            i += 1
            t = data[0][i]
            t_str=data[1][i]
            data[0][i] = data[0][j]
            data[1][i] = data[1][j]
            data[0][j] = t
            data[1][j] = t_str
    t = data[0][i+1]
    t_str=data[1][i+1]
    data[0][i+1] = data[0][r]
    data[1][i+1] = data[1][r]
    data[0][r] = t
    data[1][r] = t_str
    return i+1

def quickSort(data,p,r):
    if p < r:
        q = partition(data,p,r)
        quickSort(data,p,q-1)
        quickSort(data,q+1,r)

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
            if temp>sorted_list[0][x]:
                sorted_list[0].insert(x,temp)
                sorted_list[1].insert(x,temp_str)
                break
            elif temp<=sorted_list[0][-1]:
                sorted_list[0].append(temp)
                sorted_list[1].append(temp_str)
                break
            else:
                continue
    return sorted_list



if __name__=='__main__':
    '''
    問題
    1-1,000までのランダムな数値と
    'A-Z'のアルファベットを
    要素に持つデータを10,000個を生成し、クイックソートと今までに作成した挿入ソートでソートをし、
    計算時間を比較せよ
    ただし、ソートは数値で並べ替えられるものとし、並び替え順は降順とする
    また、クイックソートが安定なソートかどうかを判定せよ
    '''
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
    # print('挿入ソート：出力データ')
    # print(output1)
    prpcess_time1 = t2 -t1

    # クリックソートで実行する
    output2=copy.deepcopy(input_data)
    t1 = time.time()
    quickSort(output2,0,len(output2[0])-1)
    t2 = time.time()
    # print('クイックソート：出力データ')
    # print(output2)
    prpcess_time2 = t2 -t1

    # 処理時間表示
    print('挿入ソートのProccess Timeは {} [s] です'.format(prpcess_time1))
    print('クイックソートのProccess Timeは {} [s] です'.format(prpcess_time2))

    # 安定なソートか判断する
    if output1==output2:
        print('安定なソートです')
    else:
        print('不安定なソートです')