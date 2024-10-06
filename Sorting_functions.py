#Bubble Sort

def BubbleSort(array, start, end):
    n = end - start + 1 
    for i in range(n-1):
        for j in range(start, end - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] 


#Selection Sort
def SelectionSort(array,start, end):
    for i in range(start ,end):
        temp=array[i]
        for j in range(i+1, end+1):
            if array[j] < temp:
                temp = j
        array[i],temp=temp,array[i]

#Insertion SOrt
def InsertionSort(array,start, end):
    for i in range(start+1,end):
        temp=array[i]
        j=i-1
        while j >=start and temp < array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=temp

#Merge Sort

def MergeSort(array, start,end):
    if start < end:
        mid_point=(start+end)//2
       
        MergeSort(array, start, mid_point)
        MergeSort(array, mid_point + 1, end)
        
        Merge(array, start, mid_point, end)
        
    
    
def Merge(array, p, q, r):
    if p != r:
        left_array= array[p:q+1]
        right_array=array[q+1:r+1]
        
        i=0
        j=0                  
        k=p
        while i<len(left_array) and j <len(right_array):
            if left_array[i] < right_array[j]:
                array[k]=left_array[i]
                i=i+1          
            else:
                array[k]=right_array[j]
                j=j+1
            k=k+1
        while i < len(left_array):
            array[k]=left_array[i]
            i=i+1 
            k=k+1
        while j < len(right_array):
            array[k]=right_array[j]
            j=j+1
            k=k+1

#Quick Sort
def partition(arr, low, high):
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1  

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

#Counting SOrt
def counting_sort(arr):
    if len(arr) <= 1:
        return arr 
    min_val=min(arr)  
    max_val=max(arr)  
    range_of_elements = max_val-min_val + 1  
    count = [0]*range_of_elements 
    for num in arr:
        count[num - min_val]+=1 
    final=[]
    for i in range(len(count)):
        final.extend([i + min_val] * count[i]) 

    return final

#Radix sort 
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp)%10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    if len(arr)== 0:
        return arr
    max_val= max(arr)
    exp=1
    while max_val // exp>0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

#Bucket Sort


def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = min(int(num * bucket_count), bucket_count - 1)  
        buckets[index].append(num)
    final=[]
    for bucket in buckets:
        InsertionSort(bucket)  
        final.extend(bucket)
    return final


#Gnome SOrt
def gnome_sort(arr):
    index = 0
    while index<len(arr):
        if index==0:
            index+=1
        if arr[index] >= arr[index - 1]:
            index+= 1
        else:
            arr[index],arr[index- 1]=arr[index- 1],arr[index]
            index-= 1
    return arr


#CockTail Shaker sort
def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return arr


#shell sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap =gap // 2
arr = [5, 1, 4, 2, 8]
shell_sort(arr)
print(arr)
