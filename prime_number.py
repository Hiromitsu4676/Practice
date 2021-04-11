def main(n):
    prime_number=[]
    for x in range(1,n+1):
        count=0
        for i in range(1,x+1):
            if x%i==0:
                count+=1
        if count==2:
            prime_number.append(x)
    return prime_number

if __name__=='__main__':
    N=10000
    rslt=main(N)
    print(rslt)
    print(len(rslt))