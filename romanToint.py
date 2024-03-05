def romanToInt(s):
    cases = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500, 
        "M": 1000
    }

    total = 0
    prev_value = 0

    for char in s:
        value = cases.get(char, "Invalid")
        
        if value == "Invalid":
            return "Invalid"
        
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        
        prev_value = value
        
    return total
    


print(romanToInt("IIII"))

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.