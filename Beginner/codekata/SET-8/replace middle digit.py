a=str(raw_input())
b=len(a)
for i in range(1,b):
    if(b%i!=0 and i%2!=0):
        c=b/2+1
        d=a[c]
print(a.replace(d,'*'))
