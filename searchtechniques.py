#linear search
"""def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[14,7,22,5,10,8]
target=10
idx=linear_search(arr,target)
print(f"Found at index {idx}")"""

#binary search
"""def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[10,20,30,40,50,60,70,80,90]
target=90
idx=binary_search(arr,target)
print(f"Found at index {idx}") """     

#using alphabets
"""def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=['A','E','I','O','U']
target='E'
idx=binary_search(arr,target)
print(f"Found at index {idx}")"""


#jump search
import math
def jump_search(arr,target):
    n=len(arr)
    step=int(math.sqrt(n))
    prev=0
    while arr[min(step,n)-1]<target:
        prev= step
        step+=int(math.sqrt(n))
        if prev>=n:
            return -1
    while arr[prev]<target:
        prev+=1
        if prev==min(step,n):
            return -1
    if arr[prev]==target:
        return prev
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
target=10
idx=jump_search(arr,target)
print(f"Found at index {idx}")