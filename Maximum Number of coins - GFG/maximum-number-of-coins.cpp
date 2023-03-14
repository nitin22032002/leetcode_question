//{ Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution {
public:
    int maxCoins(int N, vector<int>& a) {
        vector<vector<int>> dp(N+2, vector<int>(N+2, -1));
        vector<int> nums{1};
        nums.insert(nums.end(), a.begin(), a.end());
        nums.push_back(1);
        return get(nums, 0, N+1, dp);
    }
    
    int get(vector<int>& a, int start, int end, vector<vector<int>>& dp) {
        if (start >= end) {
            return 0;
        } else if (dp[start][end] != -1) {
            return dp[start][end];
        } else {
            int ans = 0;
            for (int i = start+1; i < end; i++) {
                ans = max(ans, get(a, start, i, dp) + get(a, i, end, dp) + a[i]*a[start]*a[end]);
            }
            dp[start][end] = ans;
            return ans;
        }
    }
};

//{ Driver Code Starts.
int main(){
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int> a(n);
        for(int i=0;i<n;i++)
            cin>>a[i];
        Solution S;
        cout<<S.maxCoins(n,a)<<endl;
    }
    return 0;
}
// } Driver Code Ends