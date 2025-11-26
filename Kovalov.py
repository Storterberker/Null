import random

#this is for test
def bubble_sort(arr):
    a = arr[:]  
    n = len(a)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        n -= 1  
    return a


def selection_sort(arr):
    a = list(arr)  
    n = len(a)

    for i in range(n - 1):
        min_i = min(range(i, n), key=lambda k: a[k]) 
        a[i], a[min_i] = a[min_i], a[i]
    return a

#this is for test
def insertion_sort(arr):
    a = [x for x in arr]  
    for i in range(1, len(a)):
        item = a[i]
        j = i - 1
        while j >= 0 and a[j] > item:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = item
    return a


def run_tests():
    print("test")
    test_list = [random.randint(1, 50) for _ in range(10)]
    print("jriginal list:    ", test_list)
    print("Bubble sorted:    ", bubble_sort(test_list))
    print("selection sorted: ", selection_sort(test_list))
    print("Insertion sorted: ", insertion_sort(test_list))
    print("sorted:  ", sorted(test_list))


run_tests()