class Solution(object):
        def romanToInt(self, s: str) -> int:
            roman_map = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
            
            result = 0
            last_value = 0
            
            for char in s[::-1]:
                value = roman_map[char]
                if value < last_value:
                    result -= value
                else:
                    result += value
                    last_value = value
            
            return result
