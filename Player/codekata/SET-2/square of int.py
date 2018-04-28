a=int(raw_input())
sum=0
while(a!=0):
    n=a%10
    sum=sum+n**n
    a=a/10
print(sum)
