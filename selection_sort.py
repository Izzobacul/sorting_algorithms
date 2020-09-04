import random

def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        m = float('inf')
        mi = -1
        for j in range(i, l):
            x = arr[j]
            if x < m:
                m = x
                mi = j
        arr[i], arr[mi] = m, arr[i]
    return arr

if __name__ == '__main__':
    arr = [random.randrange(0, 100) for _ in range(100)]
    sort = selection_sort(arr)
    print(arr)
