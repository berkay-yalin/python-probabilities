# OPTN → PROB → x!
def factorial(n):
  if n == 0:
    return 1
  else:
    output = n
    for i in range(1, n):
      output *= i
    return output

# OPTN → PROB → nPr
def nPr(n, r):
  numerator = factorial(n)
  denominator = factorial(n - r)
  return int(numerator / denominator)

# OPTN → PROB → nCr
def nCr(n, r):
  numerator = factorial(n)
  denominator = factorial(r) * factorial(n - r)
  return int(numerator / denominator)
