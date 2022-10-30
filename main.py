from re import search

from main_utilities import isint, isprime

from optn_stat_dist_binomial import Bpd, Bcd, InvB

def leftside(left):
  if search('Bpd\((.*?)\)', left):
    r, n, p = search('Bpd\((.*?)\)', left).group(1).split(',')
    return rightside( Bpd(r, n, p) )

  elif search('Bcd\((.*?)\)', left):
    r, n, p = search('Bcd\((.*?)\)', left).group(1).split(',')
    return rightside( Bcd(r, n, p) )

  elif search('InvB\((.*?)\)', left):
    X, n, p = search('InvB\((.*?)\)', left).group(1).split(',')
    return rightside( InvB(X, n, p) )

def rightside(right):
  if isint(right):
    return int(right)
  return '{0:.10f}'.format(float(right)).rstrip('0')

if __name__=='__main__':
  while True:
    print( leftside(input()) )
