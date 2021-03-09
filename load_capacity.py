import time

def selection_sort(nlist):
    '''
    数値リストを小さい順に並べる
    '''
    unsorted=[nlist[i] for i in range(len(nlist))]
    sorted=[]
    for x in range(len(nlist)):
        temp=unsorted[0]
        order=0
        for i in range(len(unsorted)):
            if unsorted[i]<temp:
                temp=unsorted[i]
                order=i

        sorted.append(temp)
        del unsorted[order]
    
    return sorted

def calc(W,k):
     # 前処理
    W=selection_sort(W)
    sum_W=sum(W)
    Capacity_list=[0]*k

    # 最大積載量Pの初期値(init_P)の決定
    i=0
    init_P=max(W)
    while(1):
        if (init_P+i)*k >=sum_W:
            init_P=init_P+i
            break
        else:
            i +=1
    P=init_P

    while(1):
        # 均等に荷物を入れた時のキャパリスト算出
        while (1):
            if len(W)==0:
                break
            else:
                temp=W.pop()
                if P-Capacity_list[0]>=temp:
                    Capacity_list[0] +=temp
                    Capacity_list=selection_sort(Capacity_list)
                else:
                    break
        #過積載判断
        if max(Capacity_list)>P:
            P+=1
        else:
            break
    return P,Capacity_list


if __name__=="__main__":
    '''
    荷物の個数:n
    荷物の重さ：W
    トラックの台数：k
    トラックの最大積載量:P

    条件：
    1 ≦ n ≦ 100,000
    1 ≦ k ≦ 100,000
    1 ≦ w ≦ 100,000
    1secで処理すること
    '''

    n=5
    k=3
    W=[8,1,7,3,9,11,4,5,3]

    print('荷物リスト{}を{}台のトラックに積み込みます'.format(W,k))

    t1 = time.time()
    a,b=calc(W,k)
    t2 = time.time()
    elapsed_time = t2 -t1
    print('必要な最大積載量は{}で、積載状態は{}です'.format(a,b))
    print('Proccess Timeは {} [s] です'.format(elapsed_time))


