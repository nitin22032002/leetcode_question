//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution
{
  public:
  long long largestSumCycle(int N, vector<int> Edge)
  {
        vector<bool> visited(N,false),dp(N,false);
        long long ans=-1;
        for(int i=0;i<N;i++){
            if(!visited[i])
                ans=max(ans,get(Edge,i,visited,dp).first);
        }
        return ans;
  }
    pair<long long,int> get(vector<int> &graph,int node,vector<bool> &visited,vector<bool> &dp){
        if(dp[node])
            return {0,node};
        else if(graph[node]==-1 || visited[node])
            return {-1,-1};
        else{
            visited[node]=true;
            dp[node]=true;
            pair<long long,int> ans=get(graph,graph[node],visited,dp);
            dp[node]=false;
            if(ans.first!=-1){
                if(ans.second==-1)
                    return ans;
                else if(ans.second==node)
                    return {ans.first+node,-1};
                else
                    return {ans.first+node,ans.second};
            }
            return ans;
        }
  }
};

//{ Driver Code Starts.
signed main(){
   int tc;
   cin >> tc;
   while(tc--){
      int N;
      cin >> N;
      vector<int> Edge(N);
      for(int i=0;i<N;i++){
        cin>>Edge[i];
      }
      Solution obj;
      long long ans=obj.largestSumCycle(N, Edge);
      cout<<ans<<endl;
   }
   return 0;
}
// } Driver Code Ends