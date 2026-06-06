class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();

        vector<int> ans;
        for(int i=1;i<n;i++){
            nums[i]+=nums[i-1];
        }
        int r=nums[n-1];
        int l=0;
        for(int i=0;i<n;i++){
            ans.push_back(abs(r-l-nums[i]));
            l=nums[i];
        }
        return ans;
    }
};
