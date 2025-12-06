def binary_search(arr, target):
    """
    Perform a binary search on a sorted list to find the index of a target value.

    Args:
        arr (list): A sorted list of elements (numbers or strings).
        target (any): The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # Target was not present in the array
    return -1
