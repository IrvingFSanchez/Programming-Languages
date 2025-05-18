# Word Archivists' Trie Implementation

## 📜 Project Overview

**Course:** Programming Languages (SP25-CPSC 46000)  
**Institution:** Lewis University, Romeoville, IL  
**Developer:** Irving F. Sanchez  
**Date:** May 2025

I love using metaphors so this is a specialized team of archivists employs advanced trie structures to analyze word frequency in historical documents, beginning with the declare.txt

## 🧑‍💻 The Archivist Team

| Role | Responsibility | Key Methods |
|------|---------------|------------|
| **The Librarian** | Trie structure management | `__init__`, `clear`, `is_empty` |
| **The Lexicographer** | Word frequency analysis | `add`, `get`, `size` |
| **The Etymologist** | Prefix relationship research | `has_prefix` |

## 🛠️ Technical Implementation

### Trie Structure Design

```python
[Root]
├── a (occurrence: 16)
│   ├── b (occurrence: 0)
│   │   ├── d (occurrence: 0)
│   │   │   └── i (occurrence: 0)
│   │   │       └── c (occurrence: 0)
│   │   │           └── a (occurrence: 0)
│   │   │               └── t (occurrence: 0)
│   │   │                   └── e (occurrence: 0)
│   │   │                       └── d (occurrence: 1)
└── t (occurrence: 0)
    └── h (occurrence: 0)
        └── e (occurrence: 78)
```

### Key Features

- **Historical Text Processing**: Preserves original document integrity while normalizing case
- **Efficient Lookups**: O(L) time complexity for adds/gets (L = word length)
- **Memory Optimization**: Only stores necessary character branches

## 📊 Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| `add()` | O(L) | O(L) |
| `get()` | O(L) | O(1) |
| `has_prefix()` | O(L) | O(1) |
| `size()` | O(N) | O(1) |

## 🚀 Getting Started

### Prerequisites|

- Python 3.10+
- `declare.txt` in project root

### Installation

```bash
git clone https://github.com/IrvingFSanchez/Programming-Languages
cd Recursion-On-Tree-Project2
```

### Usage

```bash
python trie.py
```

### Expected Output

```markdown
====================================
  HISTORICAL WORD ARCHIVE INITIATIVE
====================================

Word Frequency Catalog:
a: 16
abdicated: 1
...
liberty: 1

Total Unique Words: 538
Occurrences of 'liberty': 1 #This can be changed towards the bottom of the python file
```

## ✉️ Contact

Irving F. Sanchez  
Department of Computer Science  
Lewis University
<isanchez@lewisu.edu>

Key features of this README:

1. **Visual Hierarchy** - Clear sections with icons and dividers
2. **Technical Depth** - Includes complexity analysis and structure diagrams
3. **Academic Alignment** - Explicitly ties to course requirements
4. **Style Consistency** - Maintains the archivists metaphor throughout
5. **Reproducibility** - Complete setup and testing instructions
