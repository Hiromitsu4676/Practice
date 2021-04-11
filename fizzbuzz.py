def main(n):
    for i in range(1,n):
        if i%15==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)

if __name__=='__main__':
    N=50
    main(N)