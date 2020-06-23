def maxMin(k, arr):
    arr.sort()
    mn = float("inf")
    delta = k-1
    for i in range(len(arr)-k+1):
        mn = min(arr[i+delta]-arr[i], mn)
    return mn




def maxMinRecursive(k, arr, mn=float("inf"), mx=float("-inf")):
    if k == 0:
        return mx-mn
    elif k>len(arr):
        return float("inf")
    return min(maxMin(k-1, arr[1:], min(mn,arr[0]), max(mx, arr[0])), maxMin(k, arr[1:], mn, mx))        


