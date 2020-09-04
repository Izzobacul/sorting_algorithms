import random

def bubble_sort(arr):
    l = len(arr)
    swaps = -1
    while swaps != 0:
        swaps = 0
        for i in range(1, l):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swaps += 1
    return(arr)

if __name__ == '__main__':
    arr = [random.randrange(0, 100) for _ in range(100)]
    sort = bubble_sort(arr)
    print(sort)