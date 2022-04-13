class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0 
        by = prices[0]
        for i in prices:
            # print(mx)
            if ( i - by < 0):
                by = i
            else:
                if ( i-by > mx):
                    mx = i - by 
        return mx