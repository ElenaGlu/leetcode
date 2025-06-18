class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ['(', '[', '{']
        close_list = [')', ']', '}']
        tmp = []
        flag = True
        for el in s:
            if el in open_list:
                tmp.append(el)
            else:
                idx = close_list.index(el)
                if tmp and tmp[-1] == open_list[idx]:
                    del tmp[-1]
                else:
                    flag = False
        if tmp:
            flag = False
        return flag



s = "]"
obj = Solution()
print(obj.isValid(s))