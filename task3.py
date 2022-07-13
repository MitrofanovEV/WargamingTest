def merge(arr1, arr2):
    ans = list()
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            ans.append(arr2[j])
            j += 1
        else:
            ans.append(arr1[i])
            i += 1
    for k in range(i, len(arr1)):
        ans.append(arr1[k])
    for k in range(j, len(arr2)):
        ans.append(arr2[k])
    return ans


def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        arr1 = mergeSort(arr[0:m])
        arr2 = mergeSort(arr[m:])
        return merge(arr1, arr2)
    return arr


arr = [1243, 43, 3434, 3, 4, 3, 34, 3, 4, 4, 3, 4, 34, 34, 3532532, 3, 5, 5, 35, 35, 35, 53, 5, 6165, 3]
arr = mergeSort(arr)
print(arr)
"""
Сортировка mergesort является самой оптимальной для данной задачи, ведь ее лучшее, худшее и среднее время работы
принадлежит классу O(N*log N), когда в других алгоритмах, таких как Quicksort худшее время работы может быть O(N^2)
Минусом данной сортировки является дополнительный расход памяти, однако в данной задаче этим можно пренебречь. 
"""