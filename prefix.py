def get_min_word_count(wlist):
    '''
    単語リストの中の最小文字数を取得する
    '''
    temp=len(wlist[0])
    for i in range(len(wlist)):
        if len(wlist[i])<temp:
            temp=len(wlist[i])
        else:
            pass
    min_word_count=temp
    return min_word_count

def detect_prefix(wlist):
    '''
    単語リストの最小prefixを取得する
    '''
    n=get_min_word_count(wlist)
    prefix='なし'
    for x in range(2,n):
        count=0
        for i in range(len(wlist)):
            temp_prefix=wlist[0][:x]
            if temp_prefix==wlist[i][:x]:  
                count+=1
            else:
                pass
        if count==len(wlist):
            prefix=temp_prefix
        else:
            break

    return prefix


if __name__ == '__main__':
    print('単語を入力してください(endで終了)')
    word_list = []
    while(1):
        word = input()
        if word == "end":
            break
        word_list.append(word)

    # word_list=['flower','flow','flour']
    
    print(word_list)

    rslt=detect_prefix(word_list)
    print('最大prefixは{}です'.format(rslt))




