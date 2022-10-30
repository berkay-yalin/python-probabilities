from fractions import Fraction
from copy import deepcopy

from .utilities import *

class BinomialPD:
  def validation(self):
    if any(i < 0 for i in [self.r, self.n, self.p]):
      raise ValueError("Input values must be positive")

    if isNumber(self.p):
      if 0 <= self.p <= 1:
        if isInteger(self.n):
          if isInteger(self.r):
            return True
          raise TypeError("Input value for 'r' must be an integer")
        raise TypeError("Input value for 'n' must be an integer")
      raise ValueError("Input value for 'p' must be between 0 and 1")
    raise TypeError("Input value for 'p' must be an integer or float")

  def calculate(self):
    part1 = nCr(self.n, self.r)
    part2 = (self.p ** self.r)
    part3 = (1 - self.p)
    part4 = (self.n - self.r)

    self.abs = part1 * part2 * (part3 ** part4)
    self.abs = Fraction(str(float( self.abs )))

  def configure_value(self):
    self.abs = Fraction(str(float( self.abs )))

    o_int = int(self.abs)
    o_float = float(self.abs)
    o_str = str(o_float)

    if isInteger(self.abs):
      self.value = o_int
    elif 'e-' in o_str:
      value, index = o_str.split('e-')
      value = '{:.10f}'.format(float(value)).rstrip('0')
      self.value = float( value + 'e-' + index )
    else:
      self.value = float( '{0:.10f}'.format(o_float).rstrip('0') )

  def __init__(self, r, n, p):
    self.r = r
    self.n = n
    self.p = p

    self.value = Fraction(0)
    self.abs = Fraction(0)

    self.validation()

    self.r = int(r)
    self.n = int(n)
    self.p = Fraction(str(p))

    self.calculate()
    self.configure_value()

class BinomialCD(BinomialPD):
  def calculate(self):
    for i in range(self.r + 1):
      part1 = nCr(self.n, i)
      part2 = (self.p ** i)
      part3 = (1 - self.p)
      part4 = (self.n - i)

      output = part1 * part2 * (part3 ** part4)

      self.abs += output

  def __init__(self, r, n, p):
    BinomialPD.__init__(self, r, n, p)

class InvBinomialCD:
  def validation(self):
    if any(i < 0 for i in [self.X, self.n, self.p]):
      raise ValueError("Input values must be positive")

    if isNumber(self.p):
      if 0 <= self.p <= 1:
        if isInteger(self.n):
          if 0 <= self.X <= 1:
            return True
          raise ValueError("Input value for 'X' must be between 0 and 1")
        raise TypeError("Input value for 'n' must be an integer")
      raise ValueError("Input value for 'p' must be between 0 and 1")
    raise TypeError("Input value for 'p' must be a number")

  def calculate(self):
    bounds = {}

    for i in range(0, self.n + 1):
      bounds['r_upper'] = i
      bounds['X_upper'] = BinomialCD(i, self.n, self.p).value

      if bounds['X_upper'] > self.X:
        break

    for i in reversed(range(0, self.n + 1)):
      bounds['r_lower'] = i
      bounds['X_lower'] = BinomialCD(i, self.n, self.p).value

      if bounds['X_lower'] < self.X:
        break

    bounds['upper_difference'] = bounds['X_upper'] - self.X
    bounds['lower_difference'] = self.X - bounds['X_lower']

    if bounds['upper_difference'] < bounds['lower_difference']:
       return bounds['r_lower']
    if bounds['upper_difference'] > bounds['lower_difference']:
      return bounds['r_upper']

  def __init__(self, X, n, p):
    self.X = X
    self.n = n
    self.p = p

    self.validation()

    self.X = float(self.X)
    self.n = int(n)

    self.calculate()
