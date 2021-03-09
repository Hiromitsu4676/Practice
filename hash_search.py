class Hash_search():
    def __init__(self,size,nlist):
        self.size=size
        self.nlist=nlist
        self.hash_table=[None]*size

    def hash_func(self,x):
        '''
        ハッシュ値を返す
        '''
        self.x=x
        h1=self.x%self.size
        k=1
        if self.hash_table[h1]==None:
            hash_val=h1
        else:
            while(1):
                hk=(h1+k)%self.size
                if self.hash_table[hk]==None:
                    hash_val=hk
                    break
                else:
                    k +=1
        return hash_val



    def get_hash_table(self):
        '''
        ハッシュテーブルを作る
        '''
        for i in range(len(self.nlist)):
            x=self.nlist[i]
            h1=x%self.size
            k=1
            if  self.hash_table[h1] !=None:
                while(1):
                    hk=(h1+k)%self.size
                    if self.hash_table[hk]!=None:
                        k +=1
                    else:
                        self.hash_table[hk]=x
                        break
            else:
                self.hash_table[h1]=x

        return self.hash_table

    def hash_search(self,target):
        '''
        ハッシュ探索をする
        '''
        self.target=target
        h1=self.target%self.size
        k=1
        if self.hash_table[h1]==None:
            rslt="Not found"
        elif self.hash_table[h1]==self.target:
            rslt=h1
        else:
            while(1):
                hk=(h1+k)%self.size
                if  self.hash_table[hk]==self.target:
                    rslt=hk
                    break
                else:    
                    k+=1
        return rslt


if __name__=="__main__":
    input_data= [12,2,3,13]
    size=10

    HS=Hash_search(size,input_data)
    hash_table=HS.get_hash_table()
    print('ハッシュテーブルは{}です。'.format(hash_table))

    target=3
    target_hash_index=HS.hash_search(target)
    print('{}の位置は{}です'.format(target,target_hash_index))