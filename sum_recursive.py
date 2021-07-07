def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

array = [1,2,4,5,7,9,0]

ans = sum(array)

print(ans)