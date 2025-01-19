<!DOCTYPE html>
<html>
<body>
    <h1>Searching Algorithms: Binary Search and Linear Search</h1>
    <p>In this project, I have implemented two essential searching algorithms: <strong>Linear Search</strong> and <strong>Binary Search</strong>. The goal of this exercise was to gain hands-on experience with searching techniques, improve my understanding of core data structures, and analyze the time complexity of each algorithm.</p>
    
   <h2>Purpose</h2>
    <p>The Linear Search and Binary Search algorithms serve as fundamental examples of how to search for a specific value in a dataset:</p>
    <ul>
        <li><strong>Linear Search:</strong> A straightforward algorithm that checks each element in an array sequentially.</li>
        <li><strong>Binary Search:</strong> A more efficient algorithm for sorted arrays that reduces the search space by half at each step.</li>
    </ul>
    <p>By implementing both, I have practiced:</p>
    <ul>
        <li>Iterating through arrays efficiently.</li>
        <li>Understanding the performance differences between linear and logarithmic search times.</li>
        <li>Writing clean and readable code for better understanding.</li>
    </ul>

  <h2>How to Run the Program</h2>
    <ol>
        <li>Copy the code into your preferred IDE or text editor (e.g., VS Code, PyCharm, etc.).</li>
        <li>Save the file with a <code>.py</code> extension (e.g., <code>search_algorithms.py</code>).</li>
        <li>Run the script using Python:
            <pre>python search_algorithms.py</pre>
        </li>
    </ol>

  <h2>Algorithms</h2>
    <h3>Linear Search</h3>
    <p>The Linear Search algorithm works by checking each element in the array sequentially. If a match is found, it returns the index of that element. Otherwise, it returns -1.</p>
    <p><strong>Code:</strong></p>
    <pre>
def linear_search(arr, target):
    for index, value in enumerate(arr):
        print(f"Checking index {index}, value: {value}")
        if value == target:
            return index
    return -1
    </pre>
    <p><strong>How it works:</strong></p>
    <ul>
        <li><strong>Loop:</strong> Uses <code>enumerate()</code> to iterate through the array with both index and value.</li>
        <li><strong>Comparison:</strong> Compares each value with the target. If a match is found, the index is returned.</li>
        <li><strong>Not Found:</strong> Returns <code>-1</code> if no match is found after checking all elements.</li>
    </ul>

  <h3>Binary Search</h3>
    <p>The Binary Search algorithm is much more efficient but requires the array to be sorted beforehand. It repeatedly divides the search space in half and compares the target value to the middle element.</p>
    <p><strong>Code:</strong></p>
    <pre>
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        print(f"Searching in range {arr[left:right+1]}, mid element: {arr[mid]}")
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    </pre>
    <p><strong>How it works:</strong></p>
    <ul>
        <li><strong>Calculate Middle:</strong> Determines the middle index using <code>left + (right - left) // 2</code>.</li>
        <li><strong>Compare Values:</strong> Checks if the middle element matches the target. If not, it adjusts the search space accordingly.</li>
        <li><strong>Halving Search Space:</strong> Repeats the process, halving the search space with each iteration.</li>
        <li><strong>Not Found:</strong> Returns <code>-1</code> if the target is not found.</li>
    </ul>

   <h2>Time Complexity</h2>
    <ul>
        <li><strong>Linear Search:</strong>
            <ul>
                <li><strong>Best Case:</strong> O(1) – The target is the first element.</li>
                <li><strong>Worst Case:</strong> O(n) – The target is the last element or not in the array.</li>
                <li><strong>Average Case:</strong> O(n).</li>
            </ul>
        </li>
        <li><strong>Binary Search:</strong>
            <ul>
                <li><strong>Best Case:</strong> O(1) – The middle element is the target.</li>
                <li><strong>Worst Case:</strong> O(log n) – The search space is halved in each iteration.</li>
                <li><strong>Average Case:</strong> O(log n).</li>
            </ul>
        </li>
    </ul>

  <h2>Conclusion</h2>
    <p>This project provided a deeper understanding of Linear Search and Binary Search. While Linear Search is simple, it can be inefficient for large datasets. Binary Search, with its logarithmic time complexity, is far more efficient for sorted arrays.</p>
    <p>By analyzing their time complexities, I have gained insight into when to use each algorithm depending on the dataset and the task at hand. These implementations serve as a foundation for more advanced data structures and algorithms.</p>

 <h2>LinkedIn Post</h2>
    <p>I have written a detailed LinkedIn post about this project. You can check it out here: <a href="https://www.linkedin.com/posts/danial-arif-84b7bb180_coding-datastructures-algorithms-activity-7286668335952412672-sGmk?utm_source=share&utm_medium=member_desktop"></a></p>
</body>
</html>
