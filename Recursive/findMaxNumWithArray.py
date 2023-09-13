# FIND MAX NUMBER WITH ARRAY
def findMax(arr, left, right):
    if left == right:
        return arr[left]
    
    if right == left + 1:
        return max(arr[left], arr[right])
    
    mid = (left + right) // 2
    leftMax = findMax(arr, left, mid)
    rightMax = findMax(arr, mid+1, right)

    return max(leftMax, rightMax)

arr = [3, 9, 2, 7, 5, 8]
print(findMax(arr, 0, len(arr) - 1))