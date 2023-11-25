# 실버1

n = int(input())
g = [int(input()) for _ in range(n)]
dp = [0] * 10000
dp[0] = g[0]
if n >= 2:
    dp[1] = g[0]+g[1]
if n >= 3:
    dp[2] = max(dp[0] + g[2], g[1] + g[2], dp[1])
    for k in range(3, n):
        dp[k] = max(g[k] + g[k-1] + dp[k-3], g[k]+dp[k-2], dp[k-1])
print(max(dp))