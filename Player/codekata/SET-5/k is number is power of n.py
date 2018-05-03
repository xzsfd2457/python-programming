a= int(raw_input())
b=int(raw_input())
v='no'
for i in range(1,a+1,1):
    if(b==a**i):
        v='yes'
print(v)
