from fractions import Fraction
from math import fsum

from optn_prob import factorial, nPr, nCr

'''
Probability mass function for a binomial distribution
X~B(n, p)

Binomial Probability Distribution
P(X = r)   →   Bpd(r, n, p)

Binomial Cumulative Distribution
P(X ≤ r)   →   Bcd(r, n, p)

Negative Binomial Cumulative Distribution
           →   InvB(X, n, p)
'''

# OPTN → STAT → DIST → BINOMIAL → Bpd
def Bpd(r, n, p):
  r, n, p = Fraction(r), Fraction(n), Fraction(p)

  return nCr(int(n), int(r)) * (p ** r) * ((1 - p) ** (n - r))

# OPTN → STAT → DIST → BINOMIAL → Bcd
def Bcd(r, n, p):
  return fsum([ Bpd(i, n, p) for i in range(int(r) + 1) ])

# OPTN → STAT → DIST → BINOMIAL → InvB
def InvB(X, n, p):
  X, n, p = Fraction(X), Fraction(n), Fraction(p)

  X_temp = 0
  r_temp = 0

  while X_temp < X:
    X_temp = Bcd(r_temp, n, p)
    r_temp += 1

  return r_temp - 1
