n=int(input("enter"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if n==sum:
    print("yes")
else:
    print("no")
    