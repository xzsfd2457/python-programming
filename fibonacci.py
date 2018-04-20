d=int(raw_input())
a=0
b=1
for i in range(d):
    c=a+b
    a=b
    b=c
    print(a)
	
