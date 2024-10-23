n=5
sea=[82,55,89,12,98]
def selctionsort(l1):
    for i in range(0,n):
        for j in range(i+1,n):
            if l1[i]>l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    return l1
print("sorted list using selection sort",selctionsort(sea))
                #OR/OR/OR/OR/OR
def greedy_selection_sort(arr):
    sorted_arr = []
    while arr:
        min_element = min(arr)
        sorted_arr.append(min_element)
        arr.remove(min_element)
    return sorted_arr
unsorted_list = [64, 25, 12, 22, 11]
print("Sorted array:", greedy_selection_sort(unsorted_list))