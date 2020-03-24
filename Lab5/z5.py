def combin1(n,k):
    if k==0 or n==k:
        return 1
    else:
        return combin1(n-1,k)+combin1(n-1,k-1)
n=int(input('N='))
k=[i for i in range(0,n+1)]
comb=[combin1(n,ki) for ki in k]
print('K:',k)
print('C(N,K):',comb)