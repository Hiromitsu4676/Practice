def selection_sort(nlist):
    '''
    数値リストを小さい順に並べる(選択ソート)
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

def bubble_sort(nlist):
    '''
    数値リストを小さい順に並べる(バブルソート)
    '''
    count=0
    while(1):
        for i in range(len(nlist)-1):
            front=nlist[i]
            back=nlist[i+1]
            if front>back:
                nlist[i]=back
                nlist[i+1]=front
                count+=1
        if count>0:
            count=0
        else:
            break
    return nlist


def insertion_sort(nlist):
    '''
    数値リストを小さい順に並べる(挿入ソート)
    '''
    sorted_list=[]
    sorted_list.append(nlist[0])

    for i in range(1,len(nlist)):
        temp=nlist[i]
        for x in range(i):
            if temp<sorted_list[x]:
                sorted_list.insert(x,temp) 
                break
            elif temp>=sorted_list[-1]:
                sorted_list.append(temp)
                break
            else:
                continue
    return sorted_list



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
    
    print(input_data)

    a=selection_sort(input_data)
    print('選択ソート',a)

    b=bubble_sort(input_data)
    print('バブルソート',b)

    c=insertion_sort(input_data)
    print('挿入ソート',c)

