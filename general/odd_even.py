"""""
Add a program that returns 1 if odd and 0 if even. 
Assume inputs are from 0-50000. 
Also add unit tests to cover all unit tests ( both boundary and variety)
"""""
def odd_even(num):
  if num % 2 != 0:
     return 1
  else:
     return 0 

assert(odd_even(0) == 0)
assert(odd_even(5000) == 0) 
assert(odd_even(8001) == 1)
assert(odd_even(10500)== 0)
assert(odd_even(20450) == 0)
assert(odd_even(35651) == 1 )
assert(odd_even(49999) == 1)

