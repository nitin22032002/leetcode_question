class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        vector<vector<int>> dp(multipliers.size(),vector<int>(multipliers.size(),INT_MIN));
        return get(nums,multipliers,0,nums.size()-1,0,dp);
        
    }
    int get(vector<int> &nums,vector<int> &mult,int i,int j,int k,vector<vector<int>> &dp){
        if(k>=mult.size())
            return 0;
        if(dp[i][nums.size()-j-1]!=INT_MIN)
            return dp[i][nums.size()-j-1];
        dp[i][nums.size()-j-1]= max(nums[i]*mult[k]+get(nums,mult,i+1,j,k+1,dp),nums[j]*mult[k]+get(nums,mult,i,j-1,k+1,dp));
            
        return dp[i][nums.size()-j-1];
    }
};