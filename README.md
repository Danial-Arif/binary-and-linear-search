Searching Algorithms: Binary Search and Linear Search
In this project, I have implemented two essential searching algorithms: Linear Search and Binary Search. The goal of this exercise was to gain hands-on experience with searching techniques, improve my understanding of core data structures, and analyze the time complexity of each algorithm.

Purpose
The Linear Search and Binary Search algorithms serve as fundamental examples of how we can search for a specific value in a dataset. Linear Search is a straightforward algorithm that checks each element in an array one by one, whereas Binary Search is more efficient for sorted arrays and reduces the search space by half with each step.

By implementing both, I’ve been able to practice:

Iterating through arrays.
Understanding the performance differences between linear and logarithmic search times.
Developing clear, readable code that can be easily followed and understood.
How to Run the Program
Clone this Repository
To get started with the code, first clone this repository to your local machine:

bash
Copy
Edit
git clone <repo-url>
cd <repo-directory>
Running the Linear Search
The linear_search() function works by checking each element in the array sequentially to find the target value. To run the linear search code:

bash
Copy
Edit
python linear_search.py
Example array and target value:

python
Copy
Edit
array = [4, 2, 7, 1, 9, 3, 6]
target = 9
Running the Binary Search
The binary_search() function assumes the array is already sorted and reduces the search space in half with each iteration to find the target value. To run the binary search code:

bash
Copy
Edit
python binary_search.py
Example array and target value:

python
Copy
Edit
array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
Make sure you have Python installed to execute these scripts.

Algorithms
Linear Search
The Linear Search algorithm works by checking each element in the array one by one, starting from the first element. If a match is found, it returns the index of that element. If no match is found after checking all the elements, it returns -1.

Code Explanation:

python
Copy
Edit
def linear_search(arr, target):
    for index, value in enumerate(arr):  # Loop through the array with index and value
        print(f"Checking index {index}, value: {value}")  # Debug message
        
        if value == target:  # If the current value matches the target
            return index  # Return the index where the target is found

    return -1  # Return -1 if the target is not found
Loop: I use the enumerate() function to loop through the array and get both the index and the value of each element.
Comparison: The function compares each element (value) with the target. If they match, it immediately returns the current index.
Not Found: If no match is found, the function returns -1.
Example Usage:

python
Copy
Edit
array = [4, 2, 7, 1, 9, 3, 6]
target = 9

result = linear_search(array, target)  # Call the linear_search function
If the target is found, it prints the index; otherwise, it prints "Target not found."

Time Complexity
Best Case: O(1) – If the target is the first element in the array.
Worst Case: O(n) – If the target is the last element or not in the array at all.
Average Case: O(n) – Since it may need to check each element in the array.
Binary Search
The Binary Search algorithm is much more efficient than Linear Search, but it requires the array to be sorted. Binary Search works by comparing the target value to the middle element of the array. If the middle element is the target, it returns the index. If the target is smaller, it searches the left half; if it's larger, it searches the right half, continuously halving the search space.

Code Explanation:

python
Copy
Edit
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Initialize the left and right pointers

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        print(f"Searching in range {arr[left:right+1]}, mid element: {arr[mid]}")  # Debug message

        if arr[mid] == target:
            return mid  # Return the index of the target if found
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half

    return -1  # Return -1 if the target is not found
Middle Element: The middle index mid is calculated, and the element at that index is compared to the target.
Left or Right Half: Depending on whether the middle element is smaller or larger than the target, the search space is halved. The left pointer (left) or right pointer (right) is adjusted accordingly.
Return: If the target is found, the function returns the index. If the target is not found by the time the pointers cross, it returns -1.
Example Usage:

python
Copy
Edit
array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

result = binary_search(array, target)
If the target is found, it prints the index; otherwise, it prints "Target not found."

Time Complexity
Best Case: O(1) – If the middle element is the target.
Worst Case: O(log n) – In each iteration, the search space is halved, which leads to logarithmic time complexity.
Average Case: O(log n) – Like the worst case, the average case also has a logarithmic time complexity.
Worst-case O(n): If the array is not sorted and needs to be sorted first before performing the binary search, the time complexity becomes O(n) for sorting, and binary search would add O(log n), resulting in an overall complexity of O(n log n).
Conclusion
Through this project, I gained a deeper understanding of Linear Search and Binary Search. Linear Search is simple to implement but can be inefficient for large datasets. Binary Search, on the other hand, offers logarithmic time complexity, making it a much better choice for searching within large sorted datasets.

I also explored the time complexities in both best and worst-case scenarios, understanding when and how to apply each algorithm based on the dataset and the task at hand.

I hope this code helps demonstrate the practical application of searching algorithms and serves as a solid foundation for more complex data structures and algorithms in the future.

