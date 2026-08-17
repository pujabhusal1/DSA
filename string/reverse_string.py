"""
Input : string of length <20
Output : reverse of that string

Example : "abc" -> "cba"
"" -> ""
"a" -> "a" 

Hint : Use stack
"""

def reverse_string(mystring):
    ans = ""
    for i in mystring:
        #print(i)
        ans = i + ans
    return ans
(reverse_string('puja'))

assert(reverse_string('bhusal'))=='lasuhb'
assert(reverse_string('') == '')


