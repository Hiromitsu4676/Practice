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

def get_preindex(unsorted,sorted):
    '''
    ソート前のインデックスを取得する関数
    '''
    rslt=[]
    for i in range(len(sorted)):
        temp=sorted[i]
        for j in range(len(unsorted)):
            if temp==unsorted[j]:
                rslt.append(j)
    return rslt

def binary_explore_tree(nlist,target_num):
    '''
    ターゲット数のインデックスを取得する関数（２分木探索）
    '''
    sorted_nlist=selection_sort(nlist)
    preindex=get_preindex(nlist,sorted_nlist)

    left=0
    right=len(sorted_nlist)

    while(1):
        center=int((left+right)/2)
        if target_num<sorted_nlist[center]:
            right=center
        elif target_num>sorted_nlist[center]:
            left=center
        else:
            temp_index=center
            break
    
    rslt=preindex[temp_index]
    return rslt


if __name__=='__main__':
    num_list=[10,3,5,2,9,4,12]
    target=5
    ans=binary_explore_tree(num_list,target)
    print('{}のインデックスは{}です'.format(target,ans))
