#1 + 8 + 27 …………n terms
n=int(input('enter'))
i=1
sum=0
while i<=n:
    a=i**3
    sum=sum+a
    print(a,"+",end=" ")
    i=i+1
print("=",sum)