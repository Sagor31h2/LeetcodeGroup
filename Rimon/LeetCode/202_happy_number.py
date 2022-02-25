class Solution:
    def isHappy(self, n: int) -> bool:
        # n = 2
        s = 0
        lst = []
        while s != 1:
            s = 0
            while n != 0:
                r = n %10
                s += r*r
                n= n// 10
            if s in lst:
                return False
            lst.append(s)
            # print(lst)
            n = s
            
        return True

        