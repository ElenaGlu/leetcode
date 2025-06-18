from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list_rows = [[1], [1, 1]]
        new_list = []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return list_rows
        for i in range(1, numRows - 1):
            tmp = list_rows[i]
            for j in range(len(tmp)):
                f = j + 2
                if f <= len(tmp):
                    digit_sum = sum(tmp[j:f])
                    new_list.append(digit_sum)
            new_list.insert(0, 1)
            new_list.append(1)
            list_rows.append(new_list)
            new_list = []
        return list_rows

numRows = 5
obj = Solution()
print(obj.generate(numRows))
