def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example Usage
if __name__ == "__main__":
    array = [1, 2, 3, 4, 6, 7, 9]
    target = 9

    print(f"Array: {array}")
    print(f"Target: {target}")

    result = binary_search(array, target)

    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found.")
