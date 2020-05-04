
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo = (n+1) * [0]
        memo[0] = 0
        memo[1] = 1
        for i in range(2,n+1):
            memo[i]=memo[i-2]+memo[i-1]
        return memo[n]
