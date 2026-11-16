from fractions import Fraction
import time

a = Fraction(input("Input a: "))
b = Fraction(input("Input b: "))
start = time.time()
ab = a * b
end = time.time()
print("a * b = ", ab)
print(f"Calculation took {end - start:.2f} s.")