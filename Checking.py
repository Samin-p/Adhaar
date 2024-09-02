<<<<<<< HEAD
from itertools import combinations
line2=[]
with open("Check.txt","r") as r:
    line2=[line.strip() for line in r]
    r=len(line2)
print(line2)
lis=list(range(1,r+1))
y={}

for key,value in zip(lis,line2):
    y[key]=value
def comp(dict):
    p=list(dict.keys())
    results={}

    for key1,key2 in combinations(p,2):
        x=results[(key1,key2)]=dict[key1]==dict[key2]
        if x==True:
            print(f"{key1}no. and {key2} these two are repeated")
    return results

=======
from itertools import combinations
line2=[]
with open("Check.txt","r") as r:
    line2=[line.strip() for line in r]
    r=len(line2)
print(line2)
lis=list(range(1,r+1))
y={}

for key,value in zip(lis,line2):
    y[key]=value
def comp(dict):
    p=list(dict.keys())
    results={}

    for key1,key2 in combinations(p,2):
        x=results[(key1,key2)]=dict[key1]==dict[key2]
        if x==True:
            print(f"{key1}no. and {key2} these two are repeated")
    return results

>>>>>>> e427682e452bb0172aa61ae060d12a9e2c35b172
print(comp(y))