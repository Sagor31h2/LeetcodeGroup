class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0
        while i<len(nums):
            n = nums[i]
            if nums[i] != nums[n-1]:
                nums[i],nums[n-1] = nums[n -1],nums[i]
            else:
                i+=1 
        l = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                l.append(i+1)
        return l
                