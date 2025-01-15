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

dp=[[-1 for i in range(weight+1)] for j in range(len(b)+1)]
#recursive function then to memo
# @lru_cache(maxsize=None)
# def magic(i,sum,w):
#     if i>=len(b):
#         if w==0:
#             return sum
#         else:
#             return 0
#     if w==0:
#         return sum
#     if dp[i][w]!=-1:
#         return dp[i][w]
#     if b[i]>w:
#         dp[i][w]= magic(i+1,sum,w) # non pick as weight is more 
#         return dp[i][w]
#     else:
#         dp[i][w]= max(magic(i+1,sum+c[i],w-b[i]),magic(i+1,sum,w)) # pick or non pick
#         return dp[i][w]

# print(magic(0,0,weight))


#tabulation
#base case 0 not possible (first row and first column)
for i in range(len(dp)):
    for j in range(len(dp[0])):
        if i==0 or j==0:
            dp[i][j]=0

for i in range(1,len(b)+1):
    for j in range(1,weight+1):

        if b[i-1]>j:
            # print(i)
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(c[i-1]+dp[i-1][j-b[i-1]],dp[i-1][j])

print(dp[len(b)][weight])

    


