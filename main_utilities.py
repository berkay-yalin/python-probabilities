from fractions import Fraction

def isint(x):
  if isinstance(x, int):
      return True
  elif isinstance(x, float):
    integral, fractional = str(x).split('.')
    return (True if all(i in '0' for i in fractional) else False)

  elif isinstance(x, Fraction):
    return isint(float(x))

def isprime(x):
  if x > 1 and x != 2:
      return (True if isint(x ** 0.5) == True else False)
  else:
      return False
