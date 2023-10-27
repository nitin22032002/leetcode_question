//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++

class Solution{
  public:
    int minimumNumberOfDeletions(string S) { 
        vector<vector<int>> dp(S.size(),vector<int>(S.size(),-1));
        return get(S,0,S.size()-1,dp);
    }
    int get(string &S,int i,int j,vector<vector<int>> &dp){
        if(i>=j)
            return 0;
        else if(dp[i][j]!=-1)
            return dp[i][j];
        else{
            int ans;
            if(S[i]==S[j])
                ans=get(S,i+1,j-1,dp);
            else
                ans=min(get(S,i+1,j,dp),get(S,i,j-1,dp))+1;
            dp[i][j]=ans;
            return ans;
        }
    }
};

//{ Driver Code Starts.
int main(){
    int t;
    cin >> t;
    while(t--){
        string S;
        cin >> S;
        Solution obj;
        cout << obj.minimumNumberOfDeletions(S) << endl;
    }
    return 0;
}
// } Driver Code Ends