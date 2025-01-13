from functools import lru_cache

#idea is simply using the 0/1 knapsack template

#input 
a=list(map(int,input().split()))
b=[]
c=[]
weight=a[1]
for i in range(a[0]):
    d=(list(map(int,input().split())))
    b.append(d[0])
    c.append(d[1])

#recursive function 
@lru_cache(maxsize=None)
def magic(i,sum,w):
    if i==len(b):
        return sum
    if w==0:
        return sum
    if b[i]>w:
        return magic(i+1,sum,w) # non pick as weight is more 
    else:
        return max(magic(i+1,c[i]+sum,w-b[i]),magic(i+1,sum,w)) # pick or non pick

print(magic(0,0,weight))
