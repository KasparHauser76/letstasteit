from random import *
print('have a two random sequences: ')
seq1 = [randint(1,101) for x in range(0,10)]
seq2 = [randint(1,101) for x in range(0,10)]
print(seq1,'\n', seq2)

a = set(seq1)
b = set(seq2)

intersec = a.intersection(b)
print('num have in both sequences: ', intersec)

a_minus_b = a.difference(b)  
print('num have only in first seq: ', a_minus_b)

b_munis_a = b.difference(a)
print('num have only in second seq: ', b_munis_a)

simmetric = a.symmetric_difference(b)
print('num have in first or second, but not in both: ', simmetric)