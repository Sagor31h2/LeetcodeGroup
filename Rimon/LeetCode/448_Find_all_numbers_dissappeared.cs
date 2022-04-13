public class Solution {
    public IList<int> FindDisappearedNumbers(int[] nums) {
        var l= new List<int>();
        for(int i = 0; i<nums.Length; i++){
            var n = Math.Abs(nums[i]);
            if(nums[n-1] > 0)
                nums[n-1] *= -1;            
        }
        for(int i =0; i<nums.Length; i++){
            if(nums[i] > 0){
                l.Add(i+1);
            }
        }
        return l;
    }
}