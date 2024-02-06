def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后i个元素已经到位，无需比较
        for j in range(0, n - i - 1):
            # 遍历从0到n-i-1，交换如果发现元素不按顺序
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

print("原始数组:", arr)

bubble_sort(arr)
