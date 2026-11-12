class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int n=nums.length;
        int p=1,q=1,ans=1;
        for(int i=1;i<n;i++){
            if(nums[i-1]<nums[i]){
                p++;
                ans=Math.max(ans,p);
            }
            else
                p=1;
            if(nums[i-1]>nums[i]){
                q++;
                ans=Math.max(ans,q);
            }
            else
                q=1;
        }
        return ans;
    }
}
