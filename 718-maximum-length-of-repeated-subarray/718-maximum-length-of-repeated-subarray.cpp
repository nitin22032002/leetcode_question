class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> dp(nums1.size()+1,vector<int>(nums2.size()+1,-1));
        get(nums1,nums2,0,0,dp);
        int ans=0;
        for(int i=0;i<nums1.size();i++){
            for(int j=0;j<nums2.size();j++){
                ans=max(ans,dp[i][j]);
            }
        }
        return ans;
    }
    int get(vector<int> &arr1,vector<int> &arr2,int i,int j,vector<vector<int>> &dp){
        if(i>=arr1.size() || j>=arr2.size())
            {dp[i][j]= 0;
            return 0;
             }
        else if(dp[i][j]!=-1)
            return dp[i][j];
        else
            {int take=0;
            if(dp[i+1][j]==-1)
                get(arr1,arr2,i+1,j,dp);
            if(dp[i][j+1]==-1)
                get(arr1,arr2,i,j+1,dp);
            if(dp[i+1][j+1]==-1)
                take=get(arr1,arr2,i+1,j+1,dp);
            else
                take=dp[i+1][j+1];
            if(arr1[i]==arr2[j])
                dp[i][j]= take+1;
            else
                dp[i][j]= 0;
            return dp[i][j];
             }
    }
};