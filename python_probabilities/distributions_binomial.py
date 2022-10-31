from fractions import Fraction
# from copy import deepcopy
# from operator import itemgetter

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
    self.p = Fraction(str(self.p))
    part1 = nCr(self.n, self.r)
    part2 = (self.p ** self.r)
    part3 = (1 - self.p)
    part4 = (self.n - self.r)
    self.val = part1 * part2 * (part3 ** part4)

  def configure_value(self):
    o_int = int(self.val)
    o_float = float(self.val)
    o_str = str(o_float)

    if isInteger(o_float):
      self.dis = o_int
    elif 'e-' in o_str:
      value, index = o_str.split('e-')
      value = '{:.10f}'.format(float(value)).rstrip('0')
      self.dis = float( value + 'e-' + index )
    else:
      self.dis = float( '{0:.10f}'.format(o_float).rstrip('0') )

  def __init__(self, r, n, p):
    self.r = r
    self.n = n
    self.p = p

    self.dis = Fraction(0)
    self.val = Fraction(0)

    self.validation()
    self.calculate()
    self.configure_value()

class BinomialCD(BinomialPD):
  def calculate(self):
    for i in range(int(self.r) + 1):
      part1 = nCr(self.n, i)
      part2 = (self.p ** i)
      part3 = (1 - self.p)
      part4 = (self.n - i)

      output = part1 * part2 * (part3 ** part4)

      self.val += output

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
    self.X = float(Fraction(str(self.X)))
    self.n = int(self.n)

    lower_bound = {}
    upper_bound = {}

    for i in range(0, self.n + 1):
      if BinomialCD(i, self.n, self.p).dis == self.X:
        return i

    for i in range(0, self.n + 1):
      temp_X_value = BinomialCD(i, self.n, self.p).dis
      if temp_X_value > self.X:
        upper_bound['r_value'] = i
        upper_bound['diff'] = abs( sub_f(self.X, temp_X_value) )
        break
    for i in reversed(range(0, self.n)):
      temp_X_value = BinomialCD(i, self.n, self.p).dis
      if temp_X_value < self.X:
        lower_bound['r_value'] = i
        lower_bound['diff'] = abs( sub_f(self.X, temp_X_value) )
        break

    if upper_bound['diff'] < lower_bound['diff']:
      return upper_bound['r_value']
    else:
      return lower_bound['r_value']

  def __init__(self, X, n, p):
    self.X = X
    self.n = n
    self.p = p

    self.validation()
