# 💡 Programming-Languages

---

## 🏆 Sorting Olympics: Algorithm Performance Overview (`algo-performance.py`)

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

### **1. Empirical Measurement**  

- Tracks execution time for input sizes: `[10, 100, 1000, 10000, 100000]`  
- Uses `time.perf_counter()` for precision  

### **2. Visualization**

```python
plt.xscale('log')  # Log-scale for crowd sizes  
plt.yscale('log')  # Log-scale for time  
```

![Log-Log Plot Example](https://miro.medium.com/v2/resize:fit:1400/1*5pqQ4QfX5lQkZb9y6vYvBQ.png)  
*(Example showing O(n²) vs O(n log n) slopes)*  

### **3. Original Implementations**

- No library functions used  
- Includes optimizations (e.g., Bubble Sort's early exit)  

## 🚀 How to Run

```bash
python algo-performance.py
```

---

🏛 **Lewis University, SP25-CPSC 46000
