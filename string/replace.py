"""
Input : String of length <10 characters. Has only english alphabets. 
Example : "abc", "", "abcz", "mango"
Function : replace_vowels (a-> '1', e->'2', 'i'-> '3', 'o'->'4', 'u'->'5')
'abc' -> '1bc', 'elephant' -> '2l2ph1nt', 'xyz' -> 'xyz'

Hint 1:
myString : 'x' 
myString = myString + '1' -> 'x1'

Hint 2: 
myString ='xyz' 
Iterate : It is similar to list. 
for i in range(len(myString)):
    print(myString[i])
"""
def replace_vowels(mystring):
    vowels = {
        'a': '1','e': '2', 'i': '3', 'o': "4", 'u':"5"
    }
    result = ""

    for i in range(len(mystring)):
        current_char = mystring[i]
        #print(current_char)
        if current_char in vowels:
            result = result + vowels[current_char]
            #print(result)
        else:
            result = result + current_char
            #print(result)
    return result

assert(replace_vowels('') == '')
assert(replace_vowels('a')== '1')
assert(replace_vowels('dd')== 'dd')
assert(replace_vowels('airplanees') == '13rpl1n22s')
assert(replace_vowels('abc') == '1bc')
assert(replace_vowels("samsung") == "s1ms5ng")
assert(replace_vowels("airplane") == "13rpl1n2")
assert(replace_vowels("cpccs")== "cpccs")
assert(replace_vowels("22rrrr") == "22rrrr")




