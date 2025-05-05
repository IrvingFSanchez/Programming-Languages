# Name: Irving F. Sanchez
# Course: Programming Languages SP25-CPSC 46000
# School: Lewis University, Romeoville, IL
# Purpose: This file contains the Polynomial class which represents a polynomial and provides methods for polynomial operations.


class Polynomial:
    """The Polynomial class:
    argument list: [a0, a1, a2, ... , an] which represents a0 + a1x^1 + a2x^2 + ... + anx^n

    For Example:
    p = Polynomial([1, 2, 3])
    pints as  1 + 2x + 3x^2
    """

    # =====================================
    #    CONSTRUCTOR
    # =====================================
    def __init__(self, *coefficients):
        """
        This Initializes the polynomial by triming trailing zeros and handling any empty input
        """
        # Here we remove trailing zeros to simplify the polynomial
        self.coeffs = list(coefficients)
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()
        # If the polynomial is empty, we set it to 0
        if not self.coeffs:
            self.coeffs = [0]

    # =====================================
    #    EVALUATE POLYNOMIAL (__call__)
    # =====================================
    def __call__(self, x):
        """
        This evaluates the polynomial at a given value of x

        Args:
            x (int/float): The value to evaluate the polynomial at

        Returns:
            int/float: The result of the polynomial evaluation
        """

        result = 0
        for exponent, coeff in enumerate(self.coeffs):
            result += coeff * (x**exponent)
        return result

    # =====================================
    #    DIMENSION METHOD (HIGHEST DEGREE)
    # =====================================
    def dim(self):
        """
        This returns the highest degree of the polynomial
        """
        return max(0, len(self.coeffs) - 1)

    # =====================================
    #    ADDITION OPERATOR (+)
    # =====================================

    def __add__(self, other):
        """
        This adds two polynomials together
        """

        # Here we are just going to pad the shorter polynomial with zeros
        max_length = max(len(self.coeffs), len(other.coeffs))
        padded_self = self.coeffs + [0] * (max_length - len(self.coeffs))
        padded_other = other.coeffs + [0] * (max_length - len(other.coeffs))

        # Then we just add the two polynomials together
        result_coeffs = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(*result_coeffs)

    # =====================================
    #    SUBTRACTION OPERATOR (-)
    # =====================================
    def __sub__(self, other):
        """
        This subtracts one polynomial from another
        """
        # Pad the shorter polynomial with zeros
        max_length = max(len(self.coeffs), len(other.coeffs))
        padded_self = self.coeffs + [0] * (max_length - len(self.coeffs))
        padded_other = other.coeffs + [0] * (max_length - len(other.coeffs))

        # Subtract the coefficients
        result_coeffs = [a - b for a, b in zip(padded_self, padded_other)]
        return Polynomial(*result_coeffs)
    
    # =====================================
    #    STRING REPRESENTATION (__str__)
    # =====================================
    def __str__(self):
        """
        This returns a string representation of the polynomial
        """
        terms = []
        for exponent, coeff in enumerate(self.coeffs):
            if coeff == 0 and len(self.coeffs) > 1:
                continue  # Skip zero coefficients unless it's the only term
            term = f"{coeff}"
            if exponent >= 1:
                term += f"x^{exponent}"
            terms.append(term)
        return " + ".join(terms) if terms else "0"

    __repr__ = __str__  # For the interactive interpreter


# =====================================
#    TEST CASES FOR POLYNOMIAL CLASS
# =====================================
print("\nTesting Polynomial Class:")
print("-------------------------")

# ---------------------------------------------------------------------
# Test 1: Empty Polynomial (No arguments)
# ---------------------------------------------------------------------
p0 = Polynomial()
print(f"p0 = {p0}")               # Expected: 0
print(f"p0(5) = {p0(5)}")         # Expected: 0 (0 evaluated at x=5)
print(f"p0.dim() = {p0.dim()}\n") # Expected: 0 (only a0 term exists)

# ---------------------------------------------------------------------
# Test 2: Polynomial with Trailing Zeros (Auto-trimmed)
# ---------------------------------------------------------------------
p1 = Polynomial(1, 0, 0)  # Coefficients: [1, 0, 0] → trimmed to [1]
print(f"p1 = {p1}")               # Expected: 1
print(f"p1(10) = {p1(10)}")       # Expected: 1 (1*10^0 = 1)
print(f"p1.dim() = {p1.dim()}\n") # Expected: 0 (highest exponent is 0)

# ---------------------------------------------------------------------
# Test 3: Polynomial with Negative Coefficients
# ---------------------------------------------------------------------
p2 = Polynomial(-2, 3, -4)
print(f"p2 = {p2}")               # Expected: -2 + 3x^1 + -4x^2
print(f"p2(2) = {p2(2)}")         # Expected: -2 + 3*2 + -4*(2^2) = -2 + 6 - 16 = -12
print(f"p2.dim() = {p2.dim()}\n") # Expected: 2

# ---------------------------------------------------------------------
# Test 4: Polynomial Addition (Different Lengths)
# ---------------------------------------------------------------------
p3 = Polynomial(1, 2)        # 1 + 2x
p4 = Polynomial(0, 0, 0, 5)  # Coefficients: [0, 0, 0, 5] → displayed as "5x^3"
p5 = p3 + p4
print(f"p3 + p4 = {p5}")          # Expected: 1 + 2x^1 + 5x^3
print(f"p5.dim() = {p5.dim()}\n") # Expected: 3

# ---------------------------------------------------------------------
# Test 5: Polynomial Subtraction (With Zero Terms Trimmed)
# ---------------------------------------------------------------------
p6 = Polynomial(2, -1, 4)    # 2 -1x^1 + 4x^2
p7 = Polynomial(2, -1, 4)    # Same as p6
p8 = p6 - p7                 
print(f"p6 - p7 = {p8}")            # Expected: 0
print(f"p8.dim() = {p8.dim()}\n")   # Expected: 0

# ---------------------------------------------------------------------
# Test 6: Polynomial with Middle Zero Term (Zero Skipped in String)
# ---------------------------------------------------------------------
p9 = Polynomial(1, 0, 3)    # Coefficients: [1, 0, 3]
print(f"p9 = {p9}")                 # Expected: 1 + 3x^2
print(f"p9.dim() = {p9.dim()}\n")   # Expected: 2

# ---------------------------------------------------------------------
# Test 7: Mixed Addition/Subtraction
# ---------------------------------------------------------------------
p10 = Polynomial(4, -2, 0, 7)  # 4 -2x^1 + 7x^3
p11 = Polynomial(1, 3, 5)      # 1 + 3x^1 + 5x^2
p12 = p10 + p11                # 5 + 1x^1 + 5x^2 + 7x^3
p13 = p10 - p11                # 3 -5x^1 -5x^2 + 7x^3
print(f"p10 + p11 = {p12}")     # Expected: 5 + 1x^1 + 5x^2 + 7x^3
print(f"p10 - p11 = {p13}")     # Expected: 3 + -5x^1 + -5x^2 + 7x^3
print(f"p12.dim() = {p12.dim()}")   # Expected: 3
print(f"p13.dim() = {p13.dim()}\n") # Expected: 3

# ---------------------------------------------------------------------
# Test 8: Large Polynomial with All Features
# ---------------------------------------------------------------------
p14 = Polynomial(0, -5, 0, 3, 0, 0, 2)  # Coefficients: [0, -5, 0, 3, 0, 0, 2] → trimmed to [0, -5, 0, 3, 0, 0, 2] (no trailing zeros)
# Trim trailing zeros check: Last coefficient is 2 (non-zero), so no trimming.
print(f"p14 = {p14}")                    # Expected: 0 + -5x^1 + 3x^3 + 2x^6
print(f"p14(2) = {p14(2)}")              # Calculates: 0 + (-5)*2 + 3*(2^3) + 2*(2^6) = 0 -10 + 24 + 128 = 142
print(f"p14.dim() = {p14.dim()}\n")      # Expected: 6
