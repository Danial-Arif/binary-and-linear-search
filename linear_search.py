def linear_search(arr, target):
    """
    Perform Linear Search on an array to find the target.

    Parameters:
        arr (list): A list of elements to search within.
        target (int or float): The value to find.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        print(f"Checking index {index}, value: {value}")  # Debug message
        
        if value == target:  # If the current value matches the target
            return index  # Return the index where the target is found

    return -1  # Return -1 if the target is not found


# Example Usage
if __name__ == "__main__":
    array = [4, 2, 7, 1, 9, 3, 6]  # Sample array
    target = 9  # Value to search for

    print(f"Array: {array}")
    print(f"Target: {target}")

    result = linear_search(array, target)  # Call the linear_search function
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found.")
