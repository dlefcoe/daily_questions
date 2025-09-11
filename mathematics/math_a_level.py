import math
from typing import List, Tuple

class RateOfChange:
    @staticmethod
    def average_rate_of_change(f, x1: float, x2: float) -> float:
        return (f(x2) - f(x1)) / (x2 - x1)

    @staticmethod
    def instantaneous_rate_of_change(f, x: float, h: float = 1e-5) -> float:
        return (f(x + h) - f(x - h)) / (2 * h)

class FactorialsCombinatorics:
    @staticmethod
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Factorial of negative number")
        return math.factorial(n)

    @staticmethod
    def nCr(n: int, r: int) -> int:
        if r < 0 or n < 0 or r > n:
            raise ValueError("Invalid values for nCr")
        return math.comb(n, r)

    @staticmethod
    def nPr(n: int, r: int) -> int:
        if r < 0 or n < 0 or r > n:
            raise ValueError("Invalid values for nPr")
        return math.perm(n, r)

class Quadratic:
    @staticmethod
    def solve_quadratic(a: float, b: float, c: float) -> Tuple[complex, complex]:
        d = b**2 - 4*a*c
        sqrt_d = math.sqrt(abs(d))
        if d >= 0:
            root1 = (-b + sqrt_d) / (2*a)
            root2 = (-b - sqrt_d) / (2*a)
        else:
            root1 = complex(-b/(2*a), sqrt_d/(2*a))
            root2 = complex(-b/(2*a), -sqrt_d/(2*a))
        return root1, root2

class SequencesSeries:
    @staticmethod
    def arithmetic_sequence_nth(a1: float, d: float, n: int) -> float:
        return a1 + (n - 1) * d

    @staticmethod
    def arithmetic_series_sum(a1: float, d: float, n: int) -> float:
        return n / 2 * (2 * a1 + (n - 1) * d)

    @staticmethod
    def geometric_sequence_nth(a1: float, r: float, n: int) -> float:
        return a1 * r ** (n - 1)

    @staticmethod
    def geometric_series_sum(a1: float, r: float, n: int) -> float:
        if r == 1:
            return a1 * n
        return a1 * (1 - r ** n) / (1 - r)

    @staticmethod
    def geometric_series_sum_infinite(a1: float, r: float) -> float:
        if abs(r) >= 1:
            raise ValueError("Infinite geometric series does not converge")
        return a1 / (1 - r)

class Calculus:
    @staticmethod
    def differentiate_polynomial(coeffs: List[float]) -> List[float]:
        n = len(coeffs) - 1
        return [coeffs[i] * (n - i) for i in range(n)]

    @staticmethod
    def integrate_polynomial(coeffs: List[float]) -> List[float]:
        n = len(coeffs)
        return [coeffs[i] / (n - i) for i in range(n)] + [0.0]

class Vectors:
    @staticmethod
    def dot_product(a: List[float], b: List[float]) -> float:
        return sum(x*y for x, y in zip(a, b))

    @staticmethod
    def cross_product(a: List[float], b: List[float]) -> List[float]:
        if len(a) != 3 or len(b) != 3:
            raise ValueError("Cross product is defined for 3D vectors only")
        return [
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ]

    @staticmethod
    def magnitude(a: List[float]) -> float:
        return math.sqrt(sum(x**2 for x in a))
    


# some examples of usage
def example_usage():

    # Factorials and Combinatorics
    print("Factorial of 5:", FactorialsCombinatorics.factorial(5))
    print("5 choose 2 (nCr):", FactorialsCombinatorics.nCr(5, 2))
    print("5 permute 2 (nPr):", FactorialsCombinatorics.nPr(5, 2))

    # Quadratic Equations
    roots = Quadratic.solve_quadratic(1, -3, 2)
    print("Roots of x^2 - 3x + 2:", roots)

    # Sequences and Series
    print("5th term of arithmetic sequence (a1=2, d=3):", SequencesSeries.arithmetic_sequence_nth(2, 3, 5))
    print("Sum of first 5 terms of arithmetic series (a1=2, d=3):", SequencesSeries.arithmetic_series_sum(2, 3, 5))
    print("5th term of geometric sequence (a1=2, r=3):", SequencesSeries.geometric_sequence_nth(2, 3, 5))
    print("Sum of first 5 terms of geometric series (a1=2, r=3):", SequencesSeries.geometric_series_sum(2,3,5))

def f(x):
    return x**2 + 2*x + 1

def example_usage_rate_of_change():
    # Rate of Change
    print("Average rate of change of f from x=1 to x=3:", RateOfChange.average_rate_of_change(f, 1, 3))
    print("Instantaneous rate of change of f at x=2:", RateOfChange.instantaneous_rate_of_change(f, 2))

    # Calculus
    coeffs = [1, -3, 2]  # Represents x^2 - 3x + 2
    print("Derivative coefficients:", Calculus.differentiate_polynomial(coeffs))
    print("Integral coefficients:", Calculus.integrate_polynomial(coeffs))

    # Vectors
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("Dot product of a and b:", Vectors.dot_product(a, b))
    print("Cross product of a and b:", Vectors.cross_product(a, b))
    print("Magnitude of vector a:", Vectors.magnitude(a))

if __name__ == "__main__":
    example_usage()
    print("\n--- Rate of Change Examples ---\n")
    example_usage_rate_of_change()