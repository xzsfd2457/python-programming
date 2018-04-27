k=int(raw_input())
n=int(raw_input())
c=[]
sum=0
for i in range(1,k+1):
    c.append(i)
for j in range(n):
    sum=sum+c[j]
print(sum)
