<<<<<<< HEAD
def quick_sort(arr, key=None, reverse=False):

    if len(arr) <= 1:
        return arr
    
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    
    if key:
        pivot_value = key(pivot)
    else:
        pivot_value = pivot
    
    left = []
    middle = []
    right = []
    
    for item in arr:
        if key:
            item_value = key(item)
        else:
            item_value = item
        
        if item_value < pivot_value:
            left.append(item)
        elif item_value == pivot_value:
            middle.append(item)
        else:
            right.append(item)
    
    if reverse:
        return quick_sort(right, key, reverse) + middle + quick_sort(left, key, reverse)
    else:
=======
def quick_sort(arr, key=None, reverse=False):
    """
    Quick Sort implementation for sorting heroes.
    
    Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n²)
    
    Space Complexity: O(log n) - recursion stack
    """
    if len(arr) <= 1:
        return arr
    
    # Choose middle element as pivot
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    
    # Get the comparison value
    if key:
        pivot_value = key(pivot)
    else:
        pivot_value = pivot
    
    # Partition into three lists
    left = []
    middle = []
    right = []
    
    for item in arr:
        if key:
            item_value = key(item)
        else:
            item_value = item
        
        if item_value < pivot_value:
            left.append(item)
        elif item_value == pivot_value:
            middle.append(item)
        else:
            right.append(item)
    
    # Recursive sort
    if reverse:
        return quick_sort(right, key, reverse) + middle + quick_sort(left, key, reverse)
    else:
>>>>>>> 1f0b11e8a8c1a7924165e5bb520ca1b3cce18a62
        return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)