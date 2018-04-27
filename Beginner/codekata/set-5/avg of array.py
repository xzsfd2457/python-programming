a=int(raw_input())
b=[]
c=0
sum=0
for i in range(1,a+1):
    b.append(i)
for j in range(a):
    sum=sum+b[j]
c=sum/a
print(c)
	
