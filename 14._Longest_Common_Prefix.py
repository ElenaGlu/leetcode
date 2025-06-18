from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        output = ''
        flag = False
        for el in first_word:
            for word in strs[1:]:
                if word.startswith(output + el):
                    flag = True
                else:
                    return output
            if flag:
                output += el
                flag = False
            if not output:
                return el
        return output

strs = [""]
obj = Solution()
print(obj.longestCommonPrefix(strs))
