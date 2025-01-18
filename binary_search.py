def binary_search(arr, target):
    """
    Perform Binary Search on a sorted array to find the target.

    Parameters:
        arr (list): A sorted list of elements to search within.
        target (int or float): The value to find.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2  # Avoids overflow in other languages

        # Debug message for the current range and mid
        print(f"Searching in range {arr[left:right+1]}, mid element: {arr[mid]}")

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half

    # Target not found
    return -1

# Example Usage
if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(f"Array: {array}")
    print(f"Target: {target}")

    result = binary_search(array, target)
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found.")
