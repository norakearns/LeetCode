class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Write an algorithm to determine if a number n is happy.

        A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits.

        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

        Those numbers for which this process ends in 1 are happy.
        Return true if n is a happy number, and false if not.

        Input: n = 19
        Output: true
        """
        def calc(n):
            list_num = list(str(n))
            res = 0
            for num in list_num:
                res += int(num)**2
            return res

        seen = set()
        while n != 1: 
            n = calc(n) 
            if n not in seen:
                seen.add(n) 
            else:
                return False

        return True
