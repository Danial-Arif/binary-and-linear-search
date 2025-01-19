def linear_search(arr, target):
    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1

# Example Usage
if __name__ == "__main__":
    array = [4, 2, 7, 1, 9, 3, 6]
    target = 9

    print(f"Array: {array}")
    print(f"Target: {target}")

    result = linear_search(array, target)

    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found.")
