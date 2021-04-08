'''
Areas on the Cross Section Diagram
地域の模式断面図が与えれらたとき、
雨が降り続けた際の洪水状況をシミュレートする

入力例.
\\\////\/\_/
この入力を受け取る時、断面図は以下のようになる
       /\/\_/
 \    /
  \  /
   \/
貯水量は9+1+3=13となる
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
            print('full')
        else:
            self.stack.append(x)
        return self.stack
    def pop(self):
        rslt=self.stack[-1]
        del self.stack[-1]
        return rslt
    def is_empty(self):
        return len(self.stack)==0

class Flood():
    '''
    貯水エリアを計算するクラス
    '''
    def __init__(self,text):
        self.text=text
        self.distance=1
        self.distance_stack=Stack()
        self.area=[]

    def calc_area(self):
        '''
        貯水面積を算出してリストに格納する
        '''
        for i in range(len(self.text)):
            if self.text[i]== '\\':
                self.distance_stack.push(self.distance)
                self.distance +=1
            elif self.text[i]=='/':
                if self.distance_stack.is_empty()==True:
                    self.distance +=1
                else:
                    temp_distance=self.distance_stack.pop()
                    temp_area=self.distance-temp_distance
                    self.area.append(temp_area)
                    self.distance +=1
            else:
                self.distance +=2
        return self.area
            
if __name__ == "__main__":
    input_text=["\\","\\","\\",'/','/','/','/','\\','/','\\','_','/']

    Fld=Flood(input_text)
    rslt=Fld.calc_area()
    ans=sum(rslt)
    print(ans)