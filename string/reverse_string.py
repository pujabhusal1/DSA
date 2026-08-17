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
    for char in mystring:
        #print(char)
        ans = char + ans
    return ans
(reverse_string('puja'))

assert reverse_string('bhusal') == 'lasuhb'
assert reverse_string('') == ''
assert reverse_string('a') == 'a'
assert reverse_string('puja bhusal') == "lasuhb ajup"
assert reverse_string('1234567890123456789') == "9876543210987654321"
assert reverse_string('aba') == "aba"


