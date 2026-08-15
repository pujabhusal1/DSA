def sum_of_squares(num):
    n = 0
    if num >= 0 and num <= 10:
            for i in range(0, num+1):
             n = n + i ** 2
             
    else:
        if num <= 0 and num >= -10:
            for i in range(num, 1):
             n = n + i ** 2

    return n

assert(sum_of_squares(0) == 0)       
assert(sum_of_squares(1) == 1)
assert(sum_of_squares(-1) == 1)
assert(sum_of_squares(-3)) == 14
assert(sum_of_squares(-9) == 285)
assert(sum_of_squares(2) == 5)
assert(sum_of_squares(8) == 204)


        
        
