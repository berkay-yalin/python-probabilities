import sys
sys.path.append('..')

from python_probabilities import *

def batch_binomial_test():
  arguments = [
    {'parameters': [7, 11, 0.33], 'answers': ['0.02834071024', '0.9917567634', '7']},
    {'parameters': [3, 17, 0.73], 'answers': ['2.894477589e-06', '3.118704015e-06', '3']},
    {'parameters': [7 ,45, 0.556], 'answers': ['2.971236765e-08', '3.45348805e-08', '7']}
  ]
  for i in arguments:
    print(f"Bpd({i['parameters']}) = {Bpd(*i['parameters'])}")
    print(f"                     {i['answers'][0]}")
    print(f"Bpd({i['parameters']}) = {Bcd(*i['parameters'])}")
    print(f"                     {i['answers'][1]}")
# batch_binomial_test()

# print('Bcd(3, 7, 0.337) =', Bcd(3, 7, 0.337))
# print( 'InvB(0.8210236572, 7, 0.337) =', InvB(0.8210236572, 7, 0.337), '\n\n')

# print('Bcd(7, 11, 0.43) =', Bcd(7, 11, 0.43))
# print( 'InvB(0.9538554996, 11, 0.43) =', InvB(0.9538554996, 11, 0.43), '\n\n')

print(
  'Bcd(r, 11, 0.45) + ### + InvB', InvB(0.77130684913, 11, 0.43)
)


print( Bcd(7, 11, 0.33) )
print( InvB(0.9917567634, 11, 0.33) )


# a = Bcd(7,11,0.33)
# print('Bcd(7,11,0.33) =', a)
# print('InvB(a, 11, 0.33) =', InvB(a, 11, 0.33) )


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

# # print( Bpd(7, 11, 0.33) )
# # print('Bpd(7,11,0.33) should give 0.02834071024\n')

# # print( Bcd(7, 11, 0.33) )
# # print('Bcd(7, 11, 0.33) should give 0.9917567634\n')

# # print( Bpd(3,17,0.73) )
# # print('Bpd(3,17,0.7) should give 1.11557969e-05\n')

# # print( Bcd(7,45,0.56) )
# # print('Bcd(7,45,0.56) should give 2.568023284e-08\n')

# # print( Bpd(3, 7, 0.73) )
# # print('Bpd(3, 7, 0.73) should give 0.07235885422\n')

# # print( Bcd(3, 7, 0.73) )
# # print('Bcd(3, 7, 0.73) should give 0.09050089479\n')

# # print( Bpd(5, 56, 0.556) )
# # print('Bpd(5, 56, 0.556) should give 2.108375094e-13\n')

# # print( Bcd(5, 56, 0.556) )
# # print('Bcd(5, 56, 0.556) should give 2.280468681e-13\n')
