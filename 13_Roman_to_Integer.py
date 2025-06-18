class Solution:
    symbol_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        tmp_list = [1000,]
        for item in s:
            digit = self.symbol_values[item]
            if tmp_list[-1] >= digit:
                tmp_list.append(digit)
            else:
                new_digit = digit - tmp_list[-1]
                tmp_list[-1] = new_digit
        return (sum(tmp_list) - 1000)

# s = "III"
# s = "LVIII"
s = "MCMXCIV"
obj = Solution()
print(obj.romanToInt(s))
