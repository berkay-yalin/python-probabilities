from re import search, findall
from fxcg50 import Bpd, Bcd

def leftside(left):
  if search('Bpd\((.*?)\)', left):
    r, n, p = search('Bpd\((.*?)\)', left).group(1).split(',')
    rightside(Bpd(r, n, p))

  elif search('Bcd\((.*?)\)', left):
    r, n, p = search('Bcd\((.*?)\)', left).group(1).split(',')
    rightside(Bcd(r, n, p))

def rightside(right):
  print( '{0:.10f}'.format(float(right)).rstrip('0') )

if __name__=='__main__':
  leftside(input()) #e.g., "Bcd(11, 97, 0.11)"
