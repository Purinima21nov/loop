n=int(input("enter"))
j=1
g=0
while j>0:
    count=0
    i=1
    while i<=n:
        if j%i==0:
            count=count+1
        i=i+1
        if count==2:
            g+=1
    j+=1
if n==g:
    print(j)
    