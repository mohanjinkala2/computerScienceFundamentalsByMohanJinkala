#Polynomial Multiplication with FFT in o(nlog(n))
import cmath
import math

def fft(a, invert=False):
    n = len(a)
    if n == 1:
        return a
    w_n = cmath.exp((2j if not invert else -2j) * math.pi / n)
    w = 1
    a_even = fft(a[0::2], invert)
    a_odd = fft(a[1::2], invert)
    y = [0] * n
    for k in range(n // 2):
        y[k] = a_even[k] + w * a_odd[k]
        y[k + n // 2] = a_even[k] - w * a_odd[k]
        w *= w_n
    if invert:
        for i in range(n):
            y[i] /= 2
    return y

def multiply(poly1, poly2):
    n = 1
    while n < len(poly1) + len(poly2):
        n *= 2
    f1 = fft(poly1 + [0]*(n - len(poly1)))
    f2 = fft(poly2 + [0]*(n - len(poly2)))
    f_res = [f1[i] * f2[i] for i in range(n)]
    result = fft(f_res, invert=True)
    return [round(x.real) for x in result]

# Example: Multiply (2 + 3x + 4x^2) and (1 + 2x)
print(multiply([2, 3, 4], [1, 2]))
# Output: [2, 7, 10, 8]  → 2 + 7x + 10x² + 8x³
