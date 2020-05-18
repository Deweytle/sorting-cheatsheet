#Bubble sort
def bubble_sort(array):
    l = len(array)
    for i in range(l):
        swap = False
        for j in range(0, l-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if swap == False:
            break

def recursive_bubble_sort(array):
    l = len(array) 
    for i in range(l):
        try:
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                array = recursive_bubble_sort(array)
        except:
            pass

#Selection sort
def selection_sort(array):
    l = len(array)
    for i in range(l):
        min_index = i
        for j in range(i,l):
            if(array[j] < array[min_index]):
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]

#Insertion sort
def insertion_sort(array):
    l = len(array)
    for i in range(1,l):
        insert = array[i]
        j = i - 1
        while j >= 0 and insert < array[j]:
            array[j+1] = array[j]
            j -=1
        array[j+1] = insert

def recursive_insertion_sort_wrapper(array):
    l = len(array)
    recursive_insertion_sort(array, l)
    
def recursive_insertion_sort(array, n):
    if n == 1:
        return

    recursive_insertion_sort(array, n - 1)
    insert = array[n-1]
    j = n - 2
    while j >= 0 and insert < array[j]:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = insert



#FUNCTION TESTING
if __name__ == '__main__':
    
    base_array = [64, 34, 25, 12, 22, 11, 90]

    recursive_bubble_sort(base_array)

    print("Sorted Array")
    print(base_array)
