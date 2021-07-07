def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while  first <= last:
    # we look for the mid division point
    midpoint = (first + last)// 2 # el double slash en python significa que va a redondear la division al siguiente numero mas cercano floor division
    if list[midpoint]  == target:
      return midpoint
    elif list[midpoint]  < target:
      first = midpoint + 1
    else:
      last = midpoint - 1
  
  return None

def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
