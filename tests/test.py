import sys
sys.path.append('..')

from python_probabilities import *

print( InvB(0.0905008948, 3, 0.73))
print('should give 1\n')

print( InvB(0.63, 11.0, 0.2) )
print('InvB(0.63, 11.0, 0.2) should give 3\n')

print( InvB(0.2, 11.0, 0.8) )
print('InvB(0.2, 11.0, 0.8) should give 8 (and warning on calculator)\n')

print( InvB(0.223, 37, 0.73) )
print('InvB(0.223, 37, 0.73) should give 25\n')

print( InvB(0.18, 88, 0.8) )
print('InvB(0.18, 88, 0.8) should give 67\n')

print( InvB(0.61, 7, 0.337) )
print('InvB(0.61, 7, 0.337) should give 3\n')

print( Bpd(7,11,0.33) )
print('Bpd(7,11,0.33) should give 0.02834071024\n')

print( Bpd(3,17,0.7) )
print('Bpd(3,17,0.7) should give 1.11557969e-05\n')

print( Bcd(7,45,0.56) )
print('Bcd(7,45,0.56) should give 2.568023284e-08\n')

print( Bpd(3, 7, 0.73) )
print('Bpd(3, 7, 0.73) should give 0.07235885422\n')

print( Bcd(3, 7, 0.73) )
print('Bcd(3, 7, 0.73) should give 0.09050089479\n')

print( Bpd(5, 56, 0.556) )
print('Bpd(5, 56, 0.556) should give 2.108375094e-13\n')

print( Bcd(5, 56, 0.556) )
print('Bcd(5, 56, 0.556) should give 2.280468681e-13\n')
