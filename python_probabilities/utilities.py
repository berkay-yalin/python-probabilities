from fractions import Fraction

### ### ### type validation ### ### ### ### ### ### ### ### ### ### ### ### ###

def isInteger(x):
  if isinstance(x, int):
      return True
  elif isinstance(x, float):
    integral, fractional = str(x).split('.')
    return (True if all(i in '0' for i in fractional) else False)
  elif isinstance(x, Fraction):
    return isInteger(float(x))
  return False

def isNumber(x):
  if isinstance(x, int) or isinstance(x, float) or isinstance(x, Fraction):
    return True
  return False

### ### ### output formatting ### ### ### ### ### ### ### ### ### ### ### ###

def rightside(right):
  if isInteger(right):
    return int(right)
  elif 'e-' in str(right):
    value, index = str(right).split('e-')
    value = '{:.10f}'.format(float(value)).rstrip('0')
    return float( value + 'e-' + index )
  return float( '{0:.10f}'.format(right).rstrip('0') )

### ### ### main utility functions ### ### ### ### ### ### ### ### ### ### ###

def factorial(n):
  if n == 0:
    return 1
  else:
    output = n
    for i in range(1, n):
      output *= i
    return output

def nPr(n, r):
  numerator = factorial(n)
  denominator = factorial(n - r)
  return int(numerator / denominator)

def nCr(n, r):
  numerator = factorial(n)
  denominator = factorial(r) * factorial(n - r)
  return int(numerator / denominator)

def sub_f(a, b): return float( Fraction(str(a)) - Fraction(str(b)) )
