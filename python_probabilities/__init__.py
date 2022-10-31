from .distributions_binomial import BinomialPD, BinomialCD, InvBinomialCD

def Bpd(r, n, p):
  return BinomialPD(r, n, p).dis

def Bcd(r, n, p):
  return BinomialCD(r, n, p).dis

def InvB(X, n, p):
  return InvBinomialCD(X, n, p).calculate()
