def nmemb_progr(b1,q,n):
    if n==1:
        return b1
    else:
        return nmemb_progr(b1,q,n-1)*q
def sum_nmemb(b1,q,n):
    if n==1:
        return b1
    else:
        return b1+nmemb_progr(b1,q,n)
b1=float(input('B1='))
q=float(input('Q='))
n=int(input('N='))
progr=[nmemb_progr(b1,q,i) for i in range(1,n+1)]
print(progr)
print(nmemb_progr(b1,q,n))
print(sum_nmemb(b1,q,n))