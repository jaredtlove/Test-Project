def bubble_sort(arr):
    """
    Sort a list of elements using the bubble sort algorithm.
    
    This function modifies the list in-place.

    Args:
        arr (list): The list of elements to sort.
    
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        swapped = False
        
        for j in range(0, n - i - 1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
            
    return arr
