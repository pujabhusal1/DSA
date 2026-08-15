def sum_of_squares(num):
    ans = 0
    if num >= 0 and num <= 10:
        for i in range(0, num+1):
            ans = ans + i ** 2
             
    elif num <= 0 and num >= -10:
        for i in range(num, 1):
            ans = ans + i ** 2
    else:
        print("invalid")
        return 0

    return ans

assert(sum_of_squares(0) == 0)       
assert(sum_of_squares(1) == 1)
assert(sum_of_squares(-1) == 1)
assert(sum_of_squares(-3)) == 14
assert(sum_of_squares(-9) == 285)
assert(sum_of_squares(2) == 5)
assert(sum_of_squares(8) == 204)
assert(sum_of_squares(12) == 0)
assert(sum_of_squares(-12) == 0)


        
        
