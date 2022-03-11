class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 1
        val = nums[0] 
        for i in range(len(nums)):
            if nums[i] != val :
                val = nums[i]
                nums[k],nums[i] = nums[i], nums[k]
                k+=1 
        return k