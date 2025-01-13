from functools import lru_cache
a=int(input())
b=dict()

@lru_cache(maxsize=None)
def magic(a):
    if a<0:
        return 0
    if a==0:
        return 1

    if a in b:
        return b[a]
    else:
        b[a]=(magic(a-1)+magic(a-2)+magic(a-3)+magic(a-4)+magic(a-5)+magic(a-6))%1000000007
        return b[a]


print(magic(a)%1000000007)