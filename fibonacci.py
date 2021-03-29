count=0

def fibonacci(i):
    
    global count
    count +=1
    if i==0:
        return 0
    if i==1:
        return 1
    return fibonacci(i-1)+fibonacci(i-2)

if __name__ == "__main__":
    i=6
    ans=fibonacci(i)
    print(ans)
    print(count)