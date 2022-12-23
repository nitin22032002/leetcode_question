//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
public:
    int maxCoins(int N, vector<int> &nums) {
        nums.push_back(1);
        nums.insert(nums.begin(),1);
        vector<vector<int>> dp(nums.size(),vector<int>(nums.size(),-1));
        int ans=get(nums,0,nums.size()-1,dp);
        return ans;
    }
    int get(vector<int> &nums,int start,int end,vector<vector<int>> &dp){
        if(start>=end)
            return 0;
        else if(dp[start][end]!=-1){
            return dp[start][end];
        }
        else{
            int ans=0;
            for(int i=start+1;i<end;i++){
                ans=max(ans,nums[i]*nums[start]*nums[end]+get(nums,start,i,dp)+get(nums,i,end,dp));
            }
        
            dp[start][end]=ans;
            return dp[start][end];
        }
        }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin>>N;
        
        vector<int> arr(N);
        for(int i=0; i<N; i++)
            cin>>arr[i];

        Solution obj;
        cout << obj.maxCoins(N, arr) << endl;
    }
    return 0;
}
// } Driver Code Ends