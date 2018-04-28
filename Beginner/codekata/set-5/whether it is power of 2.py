n=int(raw_input())
v="no"
for i in range(n+1):
    r=2**i
    if(n==r):
        v="yes"
print(v)
