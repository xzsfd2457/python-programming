a=str(raw_input())
b=len(a)
c=['a','e','i','o','u']
v='no'
for i in range(b+1):
    s=a[i]
if(s in c):
    v='yes'
print(v)
