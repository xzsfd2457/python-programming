a=int(raw_input())
c=0
if(a>=60):
    c=a/60
    d=a-c*60
else:
    d=a
print(c,d)
