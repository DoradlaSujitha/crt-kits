#bubble sort
arr=[12,77,43,36,24,19]
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swap=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if not swap:
            break
    return arr
sorted_arr=bubble_sort(arr)
print("Sorted array:",sorted_arr)


#selection sort
arr=[12,77,43,36,24,19]
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
sorted_arr=selection_sort(arr)
print("Sorted array:",sorted_arr)

#insertion sort
"""arr=[12,77,43,36,24,19]
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
sorted_arr=insertion_sort(arr) 
print("Insertion sort:",sorted_arr) """


#merge sort
arr=[10,55,8,2,99,14]
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i]);i +=1
        else:
            result.append(right[j]);j+=1
    result+=left[i:]
    result+=right[j:]
    return result
sorted_arr=merge_sort(arr) 
print("Merge sort:",sorted_arr)


#quick_sort
arr=[1,6,8,9,3,5]
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)
sorted_arr=quick_sort(arr)
print("quick_sort:",sorted_arr)