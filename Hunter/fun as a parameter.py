list=['guvi']
def Exploder(n):
    a=int(raw_input())	
    print(n*a)
def Myfun(dk,list):
    for item in list:
        dk(item)
Myfun(Exploder,list) 
