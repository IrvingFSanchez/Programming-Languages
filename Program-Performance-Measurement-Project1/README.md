# Program-Performance-Measurement-Project1

## Overview

This folder contains a program (algo_performance.py) that compares five common sorting algorithms as they might be used in an Olympic competition for better clarity. Each athlete (algorithm) has its own approach to the task, along with different performance characteristics that make the more or less suitable for various scenarios.

I will try my best to explain how each algorithm works and where each algorithm could be potentially used on top of associating each algorithm to its referenced Big-O performance. If any of this information seems a little off or could be better clarified feel free to message me to make any corrections to my understanding. This repository is primarily for my reference alongside any notes that I input into my files. Everything you see here are personal notes--I'm a bit picky and ocd about my notes.

## Sorting Algorithms Explained

### 1. Weightlifter (Selection Sort)

**How it works:**

- Scans the entire list to find the smallest element.
- Swaps it with the first unsorted position.
- Repeats this process for the remaining unsorted portion of the list.

**Performance Deep Dive**:

- **Time Complexity (O(n²))**:
  - *What it means*: For a list of size `n`, it performs ~n²/2 comparisons.
  - *Why*: It must scan all remaining elements (n, then n-1, then n-2...) for each position.
  - *Example*: Sorting 1,000 items requires ~500,000 operations.
  - *Visual*: Like checking every weight in the gym to find the lightest one... repeatedly.

- **Space Complexity (O(1))**:
  - *What it means*: Uses a constant amount of extra memory (just a few variables).
  - *Why*: It sorts "in-place" by swapping elements within the original array.

**Real-world use cases:**

- Educational purposes (simple to understand).
- Systems with extremely limited memory (embedded systems).
- When write operations are expensive (minimizes swaps to exactly n-1).

**Example:**

```python
# Before: [29, 10, 14, 37, 13]
# After each pass:
[10, 29, 14, 37, 13]  # Swapped 10 and 29
[10, 13, 14, 37, 29]  # Swapped 13 and 29
[10, 13, 14, 29, 37]  # No swap (14 already correct)
```

---

### 2. Gymnast (Insertion Sort)

**How it works:**

- Builds the sorted list one element at a time.
- Takes each new element and inserts it into its correct position in the sorted portion of the list.
- Efficient for nearly sorted data.

**Performance Deep Dive**:

- **Time Complexity**:
  - *Best Case (O(n))*: Already sorted data → only needs 1 comparison per element.
  - *Worst Case (O(n²))*: Reverse-sorted data → requires maximum comparisons/shifts.
  - *Adaptive*: Performs better on nearly-sorted data (runs in near-linear time).

- **Space Complexity (O(1))**:
  - Only needs a few temporary variables (current value, index pointers).

**Real-world use cases:**

- Online sorting (data coming in real-time).
- Small datasets (under 50 elements).
- When the list is mostly sorted (adaptive).
- Used in Timsort (Python's built-in sort) for small chunks.

**Example:**

```python
# Before: [29, 10, 14, 37, 13]
# After each insertion:
[10, 29, 14, 37, 13]  # Inserted 10 before 29
[10, 14, 29, 37, 13]  # Inserted 14
[10, 14, 29, 37, 13]  # 37 already correct
```

---

### 3. Swimmer (Bubble Sort)

**How it works:**

- Repeatedly steps through the list.
- Compares adjacent elements and swaps them if they are in the wrong order.
- Larger elements "bubble up" to their correct positions.

**Performance Deep Dive**:

- **Time Complexity**:
  - *Unoptimized*: Always O(n²) – makes n passes through n elements.
  - *Optimized*: Can be O(n) for sorted data (with early termination check).
  - *Example*: Sorting 1,000 items takes ~1,000,000 ops in worst case.

- **Space Complexity (O(1))**:
  - Only needs a single temporary variable for swaps.

**Real-world use cases:**

- Educational purposes.
- Simple embedded systems.
- Nearly sorted data (with optimization flag).
- Sometimes used in computer graphics for small datasets.

**Example:**

```python
# Before: [29, 10, 14, 37, 13]
# After each pass:
[10, 14, 29, 13, 37]  # First pass (37 bubbled to end)
[10, 14, 13, 29, 37]  # Second pass (29 bubbled up)
```

---

### 4. Marathoner (Merge Sort)

**How it works:**

- A divide-and-conquer approach.
- Recursively splits the list in half until each subsection contains one element.
- Merges the sorted halves back together.

**Performance Deep Dive**:

- **Time Complexity (O(n log n))**:
  - *Why log n?*: Dividing the list in half repeatedly creates ~log₂n levels.
  - *Why n?*: Each level requires merging all n elements.
  - *Example*: 1,000 items → 10 levels (2¹⁰≈1000), each level processes all 1,000 items → ~10,000 ops.

- **Space Complexity (O(n))**:
  - Needs temporary arrays during merging (unlike in-place sorts).
  - *Tradeoff*: Faster time but uses more memory.

**Real-world use cases:**

- External sorting (huge datasets that don't fit in memory).
- Database operations.
- Inversion counting problems.
- Stable sorting requirements (preserves original order of equal elements).
- Used in Python's built-in `sorted()` for large lists.

**Example:**

```python
# Before: [29, 10, 14, 37, 13]
# Recursive splitting:
[29, 10] [14, 37, 13]
[29] [10] [14] [37, 13]

# Merging:
[10, 29] [14] [13, 37]
[10, 14, 29] [13, 37]
```

---

### 5. Sprinter (Quick Sort)

**How it works:**

- Selects a "pivot" element.
- Partitions the list into elements less than and greater than the pivot.
- Recursively sorts each partition.

**Performance Deep Dive**:

- **Time Complexity**:
  - *Average Case (O(n log n))**: Good pivot choice divides data evenly.
  - *Worst Case (O(n²))**: Bad pivots (e.g., already sorted data with first element as pivot).
  - *Optimizations*: Median-of-three pivot selection prevents worst-case scenarios.

- **Space Complexity (O(log n))**:
  - *Why?*: Recursion depth is log n for balanced partitions.
  - *Memory Usage*: Uses stack space for recursion (better than Merge Sort's O(n)).

**Real-world use cases:**

- General-purpose sorting (most standard library implementations).
- Large datasets in memory.
- When average-case performance matters more than worst-case.
- Used in C++'s `std::sort`, Java's primitive type sorting.

**Example:**

```python
# Before: [29, 10, 14, 37, 13]
# Choosing last element as pivot (13):
[10, 13, 29, 14, 37]  # After first partition
# Then recursively sort left/right of pivot
```

---

### Performance Comparison Chart

| Algorithm        | Best Case | Average Case | Worst Case | Space  | Stable |
|------------------|-----------|--------------|------------|--------|--------|
| Selection Sort   | O(n²)     | O(n²)        | O(n²)      | O(1)   | No     |
| Insertion Sort   | O(n)      | O(n²)        | O(n²)      | O(1)   | Yes    |
| Bubble Sort      | O(n)      | O(n²)        | O(n²)      | O(1)   | Yes    |
| Merge Sort       | O(n log n)| O(n log n)   | O(n log n) | O(n)   | Yes    |
| Quick Sort       | O(n log n)| O(n log n)   | O(n²)      | O(log n)| No     |

**When to use each:**

- **Small datasets**: Insertion Sort
- **Nearly sorted data**: Insertion/Bubble Sort
- **Large datasets**: Merge Sort or Quick Sort
- **Memory constraints**: Selection Sort
- **Stability needed**: Merge Sort or Insertion Sort

---

### **Space Complexity Explained**

**Space Complexity** measures how much *additional* memory (RAM) an algorithm requires **beyond** the input data itself, as the input size grows. It answers:  
*"How much extra workspace does this algorithm need to sort my data?"*  

### **Key Concepts**

1. **Input Space vs. Auxiliary Space**  
   - **Input Space**: Memory used to store the original data (e.g., your unsorted list).  
   - **Auxiliary Space**: Extra memory the algorithm needs *temporarily* to perform its work.  
   - *Space Complexity focuses on **auxiliary space**.*  

2. **Notation (Big-O)**  
   - **O(1)**: Fixed memory (e.g., a few variables).  
   - **O(n)**: Scales linearly with input size (e.g., a temporary array).  
   - **O(log n)**: Grows logarithmically (common in recursive algorithms).  

---

### **Examples by Algorithm**

#### **1. O(1) Space (In-Place Sorting)**

**Algorithms**: Selection Sort, Insertion Sort, Bubble Sort  
**Why**:

- Only a few variables (e.g., loop counters, swap temp) are needed.
- They sort by *swapping elements within the original array*.  

**Visual**:  

```python
def selection_sort(arr):
    for i in range(len(arr)):       # O(1) space (single variable `i`)
        min_idx = i                 # O(1)  
        for j in range(i+1, len(arr)):  # O(1)  
            if arr[j] < arr[min_idx]:  
                min_idx = j        # O(1)  
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # In-place swap  
```

#### **2. O(n) Space (Not In-Place)**

**Algorithms**: Merge Sort  
**Why**:  

- Needs temporary arrays to merge sorted halves.  
- For 1,000 elements, it might use ~1,000 extra slots in memory.  

**Visual**:  

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]    # Temporary left half (O(n/2) space)  
        right = arr[mid:]   # Temporary right half (O(n/2) space)  
        merge_sort(left)    # Recursion adds stack frames (O(log n))  
        merge_sort(right)  
        merge(left, right)  # Merging requires O(n) space  
```

#### **3. O(log n) Space**  

**Algorithms**: Quick Sort (optimized)  
**Why**:

- Recursion depth is *logarithmic* (good pivot choice splits data evenly).  
- Each recursive call uses stack space, but not full copies of the data.  

**Example**:  
Sorting 1,024 elements → Recursion depth ~10 (since 2¹⁰ = 1024).  

---

### **Why Space Complexity Matters**

| Scenario                     | Priority                        | Ideal Algorithm          |  
|------------------------------|---------------------------------|--------------------------|  
| Embedded systems (limited RAM) | Minimize auxiliary space       | **Selection Sort (O(1))** |  
| Sorting 1TB of data           | Speed over memory              | **Merge Sort (O(n))**     |  
| General-purpose sorting       | Balance speed and memory       | **Quick Sort (O(log n))** |  

---

### **Real-World Analogy**

Imagine organizing books on a shelf:

- **O(1) Space**: You swap books in place (no extra shelf needed).  
- **O(n) Space**: You need a second shelf to temporarily hold books while reorganizing.  
- **O(log n) Space**: You use a small notebook to track where books should go.
