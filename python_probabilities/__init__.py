from .distributions_binomial import BinomialPD, BinomialCD, InvBinomialCD

def Bpd(r, n, p):
  return BinomialPD(r, n, p).value

def Bcd(r, n, p):
  return BinomialCD(r, n, p).value

def InvB(X, n, p):
  return InvBinomialCD(X, n, p).calculate()
