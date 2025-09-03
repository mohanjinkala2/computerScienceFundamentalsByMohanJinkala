def Sieve_of_Eratosthenes(n):
    isPrime=[True]*(n+1)
    isPrime[0]=isPrime[1]=False
    p=2
    while p*p<=n:
        if isPrime[p]:
           for i in range(p*p,n+1,p):
               isPrime[i]=False
        p+=1
    primeNumber=[i for i in range(len(isPrime)) if isPrime[i]==True]
    return primeNumber
print(Sieve_of_Eratosthenes(30))