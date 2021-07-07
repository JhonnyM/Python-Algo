def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <=  pivot ]

        greater = [i for i in array[1:] if i > pivot]

        return qsort(less) +  [pivot] + qsort(greater)

print (qsort([5,6,2,8,9,13,90]))
