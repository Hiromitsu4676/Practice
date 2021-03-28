class Stack():
    '''
    スタック（先入れ後だし）
    '''
    def __init__(self,size=100):
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


class ReversePolishNotation():
    '''
    逆ポーランド記法
    '''
    def __init__(self,data):
        self.data= data
        self.stack=Stack()

    def calc(self):
        for i in range(len(self.data)):
            if self.data[i]=='+':
                temp=self.stack.pop()+self.stack.pop()
                self.stack.push(temp)
            elif self.data[i]=='-':
                temp=self.stack.pop()-self.stack.pop()
                self.stack.push(temp)
            elif self.data[i]=='*':
                temp=self.stack.pop()*self.stack.pop()
                self.stack.push(temp)
            elif self.data[i]=='/':
                temp=self.stack.pop()/self.stack.pop()
                self.stack.push(temp)
            else:
                self.stack.push(int(self.data[i]))
        return self.stack.pop()

if __name__ == "__main__":
    # print('入力してください')
    # input_data = input()

    input_data='1 2 + 5 4 + *'
    input_data=input_data.split()
    print(input_data)

    RPN=ReversePolishNotation(input_data)
    ans=RPN.calc()
    print(ans)


