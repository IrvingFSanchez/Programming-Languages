# 💡 Programming-Languages

---

## 🏆 Sorting Olympics: Project 1 (`algo-performance.py`)

**An empirical study of sorting algorithms through athletic metaphors**  
*"Where O(n²) meets O(n log n) in the arena of computational efficiency!"*  

- **Five sorting algorithms** personified as Olympic athletes  
- **Log-log visualization** showing growth rates  
- **Creative metaphors** making complexity tangible  
- **Complete from-scratch implementations**  

### 🏅 The Athletes  

| Athlete              | Algorithm      | Time Complexity | Space Complexity | Signature Move          |
|----------------------|----------------|------------------|-------------------|-------------------------|
| **Weightlifter**     | Selection Sort | O(n²)            | O(1)              | "Find-and-Swap"         |
| **Gymnast**          | Insertion Sort | O(n²) (O(n) best)| O(1)              | "Flexible Positioning"  |
| **Swimmer**          | Bubble Sort    | O(n²)            | O(1)              | "Bubble Up"             |
| **Marathoner**       | Merge Sort     | O(n log n)       | O(n)              | "Divide & Conquer"      |
| **Sprinter**         | Quick Sort     | O(n log n) avg   | O(log n)          | "Pivot Dash"            |

### 🔬 Key Features

- **Empirical Measurement**: Tracks execution time for input sizes `[10, 100, 1000, 10000, 100000]`  
- **Visualization**: Log-log plots comparing algorithm performance  
- **Original Implementations**: No libraries used; optimizations like Bubble Sort’s early exit  

```bash
python algo-performance.py
```

---

## 🧩 String & Algorithm Challenges: Week 4 (`stringindex.py`)

**Five mini-algorithms showcasing string manipulation and problem-solving**  
*"From pattern extraction to tower art!"*  

### 🎯 Challenges

1. **String Indexing**: Extract every 3rd character in blocks of 6.  
   - Example: `"abcdefghijkl"` → `"abcghi"`  
2. **Pattern Locator**: Find all starting indices of a substring.  
3. **Parentheses Checker**: Validate balanced parentheses in expressions.  
4. **Tower Printer**: Generate ASCII art towers with dynamic spacing.  
5. **Missing Number**: Gauss’ formula to find the missing integer in \( 1 \dots n \).  

### 🛠️ Implementation Highlights

- **Efficiency**: Sliding window for pattern matching (\(O(n)\)).  
- **Edge Cases**: Handles unbalanced parentheses and missing number edge conditions.  

```bash
python stringindex.py
```

---

## 📈 Polynomial Arithmetic: Week 6 (`Polynomial.py`)

**A class-based implementation of polynomial operations**  
*"Where algebra meets code!"*  

### 🧮 Key Features  

- **Class Design**:  
  - Coefficients stored with trailing zeros auto-trimmed.  
  - Handles edge cases (empty input, single term).  
- **Operations**:  
  - **Arithmetic**: Addition (`+`), subtraction (`-`).  
  - **Evaluation**: Compute \( P(x) \) for any \( x \).  
  - **String Representation**: Human-readable format (e.g., `1 + 3x^2`).  
- **Test Cases**:  
  - Validates trimming, arithmetic, negative/middle-zero coefficients, and edge cases.  

```bash
python Polynomial.py
```

---

🏛 **Lewis University, SP25-CPSC 46000**
