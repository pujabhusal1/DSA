"""
Function : get_char_sum()
Input : Two strings : num1 and num2. Each string contains only digits.
Output : Returns the sum of the two numbers represented by the strings.

Assumptions : Input will be less than 10 chars. 
Compute only if input length is same. if length is different  return "invalid_input"

Example :  get_char_sum("123", "456") -> "579"
           get_char_sum("123", "45") -> "invalid_input"
           get_char_sum("923", "917") -> "18310"
           "", "" -> "0" 

Hint : Type casting
char to int : a = "1"; int(a)-> 1
int to char : a = 1; str(a) -> "1" 
"""
def get_char_sum(num1, num2):
    size1 = len(num1)
    size2 = len(num2)

    if size1 != size2:
       return "invalid_input"
    
    ans = ""
    for i in range(size1):
        char1 = num1[i]
        char2 = num2[i]
        total = int(char1) + int(char2)
        ans = ans + str(total)

    print(ans)
    return ans
#get_char_sum("88", "88")

assert (get_char_sum("", "") == "")  
assert (get_char_sum("11", "11") == "22")
assert (get_char_sum("222", "22") == "invalid_input")
assert (get_char_sum("9999", "9999") == "18181818")


"""
"120" -> 120
"220" -> 220 -> 340

"99"
"22" -> 121 -> 1111
"""




