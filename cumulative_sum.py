N=5
K=3
A=[2,5,-4,10,3]

CUSUM=[0]
temp=0
for i in range(N):
    temp+=A[i]
    CUSUM.append(temp)

rslt=set()
for j in range(0,N-K+1):
    s=CUSUM[j+K]-CUSUM[j]
    rslt.add(s)

print(max(rslt))