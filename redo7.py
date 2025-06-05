nums = [1,2,4,6]
n = len(nums)
suff = [0]*n
pre = [0]*n

suff[0] = 1
pre[n-1]=1

for i in range(1,n):
    suff[i] = suff[i-1]*nums[i-1]

for i in range(n-2,-1,-1):
    pre[i] = pre[i+1]*nums[i+1]

res = []
for i in range(n):
    res.append(pre[i]*suff[i])

print(res)