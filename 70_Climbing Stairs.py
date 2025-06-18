class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else:
            lst = [1, 2]
            for i in range(2, n):
                digit_sum = sum(lst)
                lst.append(digit_sum)
                lst.pop(0)
            return digit_sum



n = 4
obj = Solution()
print(obj.climbStairs(n))