d=int(raw_input())
e=[]
a=0
b=1
for i in range(d):
    c=a+b
    a=b
    b=c
    e.append(a)
print(e)
    
