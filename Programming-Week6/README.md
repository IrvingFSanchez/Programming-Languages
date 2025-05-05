# Polynomial Class

A Python class to represent and manipulate polynomials. Built for Lewis University's Programming Languages course (SP25-CPSC 46000).

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Flexible Initialization**: Create polynomials from `a₀` to `aₙ` coefficients
- **Mathematical Operations**: Add/subtract polynomials using `+` and `-` operators
- **Evaluation**: Compute `p(x)` for any value of x
- **Clean Display**: Human-readable string representation with automatic zero-term skipping
- **Dimension Detection**: `dim()` method returns highest degree

## Installation

Clone the repository:

```bash
git clone https://github.com/IrvingFSanchez/Programming-Languages
```

## Usage

### Basic Polynomial Operations

```python
# Create polynomials
p0 = Polynomial()          # 0
p1 = Polynomial(1, 2, 3)   # 1 + 2x + 3x²
p2 = Polynomial(0, 0, 5)   # 5x²

# Evaluate at x=2
print(p1(2))  # Output: 17 (1 + 4 + 12)

# Add polynomials
p3 = p1 + p2  # 1 + 2x + 8x²
print(p3)     # Output: 1 + 2x^1 + 8x^2

# Get polynomial degree
print(p3.dim())  # Output: 2
```

### Advanced Features

```python
# Handle negative coefficients
p4 = Polynomial(2, -1, 0, 4)  # 2 - x + 4x³
print(p4)                     # Output: 2 + -1x^1 + 4x^3

# Mixed operations
p5 = p4 - Polynomial(1, 1, 1)
print(p5)  # Output: 1 + -2x^1 + -1x^2 + 4x^3
```

## Running Tests

The included test suite validates all core functionality:

```bash
python polynomial.py
```

## Implementation Details

### Key Methods

- `__init__(*coefficients)`: Auto-trims trailing zeros
- `__call__(x)`: O(n) evaluation using Horner's method
- `__add__/__sub__`: Term-wise operations with zero-padding
- `__str__`: Intelligent formatting for human readability

## License

MIT License - See [LICENSE](LICENSE) for details.

## Acknowledgments

Developed for **Lewis University** Programming Languages course.  
Instructor: [Professor Eric Chou]  
Algorithm Inspiration: Carl Friedrich Gauss (Polynomial Summation)
