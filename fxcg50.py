from fractions import Fraction
from math import fsum

### OPTN → PROB
def factorial(n):
  if n == 0:
    return 1
  else:
    output = n
    for i in range(1, n):
      output *= i
    return output

def nCr(n, r):
  numerator = factorial(n)
  denominator = factorial(r) * factorial(n - r)
  return Fraction(numerator, denominator)

def nPr(n, r):
  numerator = factorial(n)
  denominator = factorial(n - r)
  return Fraction(numerator, denominator)

### OPTN → STAT → DIST → BINOMIAL
def Bpd(r, n, p):
  r = Fraction(r)
  n = Fraction(n)
  p = Fraction(p)
  return ( nCr(int(n), int(r)) * (p**r) * ((1-p)**(n-r)) )

def Bcd(r, n, p):
  return fsum([ Bpd(i, n, p) for i in range(int(r) + 1) ])

def InvB(x, n, p):
  pass
