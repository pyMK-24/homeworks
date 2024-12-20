def bubble_sort(arr):
    n = len(arr)

    for run in range(n):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

bubble = [7,1,3,6,4,2,8,9,5]
list_bubble = bubble_sort(bubble)
print(list_bubble)

def binary_search(A,Vall):
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1

    while First <= Last:
        Middle = (First + Last) // 2
        if Vall == A[Middle]:
            First = Middle
            Last = First
            ResultOk = True
            Pos = Middle
            break
        elif Vall > A[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk == True:
        print(f"Элемент найден {Pos}")
    else:
        print("Элемент не найден")

A = [1,2,3,4,5,6,7,8,9,10]
val = 7
binary_search(A,val)



