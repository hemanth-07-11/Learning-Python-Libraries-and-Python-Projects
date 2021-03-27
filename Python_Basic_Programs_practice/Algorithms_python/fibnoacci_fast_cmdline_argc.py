import sys
from typing import Tuple

def fibonacci(n: int) -> int:

    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return _fib(n)[0]

def _fib(n: int) -> Tuple[int, int]:
    if n == 0: 
        return (0, 1)

    a, b = _fib(n // 2)
    c = a * (b * 2 - a)
    d = a * a + b * b
    return (d, c + d) if n % 2 else (c, d)

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(f"fibonacci({n}) is {fibonacci(n)}")
