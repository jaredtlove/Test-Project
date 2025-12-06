from binary_search import binary_search
from bubble_sort import bubble_sort

def example_binary_search():
    """
    Demonstrate the usage of the binary_search function.
    """
    print("--- Binary Search Example ---")
    sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    
    print(f"List: {sorted_list}")
    print(f"Target: {target}")
    
    result = binary_search(sorted_list, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in list")
    print()

def example_bubble_sort():
    """
    Demonstrate the usage of the bubble_sort function.
    """
    print("--- Bubble Sort Example ---")
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Unsorted list: {unsorted_list}")
    
    sorted_list = bubble_sort(unsorted_list.copy())
    
    print(f"Sorted list:   {sorted_list}")
    print()

def main():
    """
    Main entry point to run examples.
    """
    example_binary_search()
    example_bubble_sort()

if __name__ == "__main__":
    main()
