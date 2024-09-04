p=int(input("enter the first number"))
i=int(input("enter the last number"))
r=[]

def main(sel):
    p=0
    for i in range(1,sel+1):
        if sel%i==0:
            p+=1
    if p==2:
        r.append(sel)
for o in range(p,i+1):
    main(o)
print(r)




