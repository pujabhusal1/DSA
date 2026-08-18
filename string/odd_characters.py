"""
Create a new string from characters in odd position only. First one is 0th position. 

"abc" -> "b"
"abcdef" -> "bdf" 

Assume : Max string size is 20.
"""
def odd_string(mystring):
    ans = ""
    for i in range(len(mystring)):
       # print(mystring[i])    
        if i % 2 == 1:
            ans = ans + mystring[i]
            #print(ans)
        #else:
            #print('no')
    return ans

assert(odd_string('') == '')
assert(odd_string('puja') == 'ua' )
assert(odd_string('kanxabhusal') == 'axbua')
assert(odd_string('123456puja1234') == '246ua24')