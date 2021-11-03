#print odd or even :

def some(n):
    if n%2==0 :
        for i in range(0,n+1,2):
            yield(i)
    else:
        for i in range(1,n+1,2):
            yield(i)


