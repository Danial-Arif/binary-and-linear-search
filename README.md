# **Searching Algorithms: Binary Search and Linear Search**

In this project, I have implemented two essential searching algorithms: **Linear Search** and **Binary Search**. The purpose of this exercise was to implement and understand these algorithms, learn their time complexities, and practice coding techniques.

## **Purpose**

This project focuses on two common searching algorithms:

- **Linear Search:** A simple search algorithm that checks each element in a list sequentially to find the target value.
- **Binary Search:** A more efficient algorithm that only works on sorted arrays, cutting the search space in half at each step.

## **How to Run the Program**

### **Running the Linear Search**

1. Copy the **Linear Search** code into your preferred IDE or text editor (e.g., VS Code, PyCharm, etc.).
2. Save the file with the name `linear_search.py`.
3. Run the script using Python:

   ```bash
   python linear_search.py
   ```

### **Running the Binary Search**

1. Copy the **Binary Search** code into your preferred IDE or text editor (e.g., VS Code, PyCharm, etc.).
2. Save the file with the name `binary_search.py`.
3. Run the script using Python:

   ```bash
   python binary_search.py
   ```

## **Algorithms**

### **Linear Search**

The **Linear Search** algorithm works by checking each element in the array sequentially. If a match is found, it returns the index of that element. Otherwise, it returns `-1`.

#### **Code:**

```python
def linear_search(arr, target):
    for i in range(len(arr)):  # Iterate using indices
        print(f"Checking index {i}, value: {arr[i]}")  # Debug message
        
        if arr[i] == target:  # Check if the current element matches the target
            return i  # Return the index if found

    return -1  # Return -1 if the target is not found
```

#### **How it works:**

- **Iteration:** The `for` loop iterates through the array using the index.
- **Comparison:** Each element is compared to the target. If a match is found, the index is returned.
- **Return Value:** If no match is found after checking all elements, `-1` is returned.

---

### **Binary Search**

The **Binary Search** algorithm is much more efficient than Linear Search, but it requires the array to be sorted beforehand. It repeatedly divides the search space in half and compares the target value to the middle element.

#### **Code:**

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1  # Define the initial search boundaries

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        print(f"Low: {low}, High: {high}, Mid: {mid}, Value: {arr[mid]}")  # Debug message
        
        if arr[mid] == target:  # If the middle element is the target
            return mid  # Return the index if found
        elif arr[mid] < target:  # If the target is larger than the middle element
            low = mid + 1  # Narrow the search to the upper half
        else:  # If the target is smaller than the middle element
            high = mid - 1  # Narrow the search to the lower half

    return -1  # Return -1 if the target is not found
```

#### **How it works:**

- **Search Space Halving:** The search space is repeatedly halved by comparing the middle element with the target.
- **Mid Calculation:** The midpoint index is calculated as `low + (high - low) // 2` to avoid overflow.
- **Return Value:** If the target is found, the index is returned. Otherwise, `-1` is returned.

---

## **Time Complexity**

### **Linear Search:**

- **Best Case:** O(1) – The target is the first element.
- **Worst Case:** O(n) – The target is the last element or not in the array.
- **Average Case:** O(n).

### **Binary Search:**

- **Best Case:** O(1) – The middle element is the target.
- **Worst Case:** O(log n) – The search space is halved in each iteration.
- **Average Case:** O(log n).

---

## **Conclusion**

This project helped me gain a deeper understanding of **Linear Search** and **Binary Search**. While **Linear Search** is simple and works on unsorted arrays, it can be inefficient for large datasets. On the other hand, **Binary Search** is efficient for sorted arrays with a time complexity of O(log n), making it far more suitable for large datasets.

---

## **LinkedIn Post**

I have written a detailed LinkedIn post about this project. You can check it out here: <a href="https://www.linkedin.com/posts/danial-arif-84b7bb180_coding-datastructures-algorithms-activity-7286668335952412672-sGmk?utm_source=share&utm_medium=member_desktop"> View Post</a>
