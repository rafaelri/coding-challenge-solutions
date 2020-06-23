def maxMin(k, arr, mn=float("inf"), mx=float("-inf")):
    if k == 0:
        return mx-mn
    elif k>len(arr):
        return float("inf")
    return min(maxMin(k-1, arr[1:], min(mn,arr[0]), max(mx, arr[0])), maxMin(k, arr[1:], mn, mx))        


