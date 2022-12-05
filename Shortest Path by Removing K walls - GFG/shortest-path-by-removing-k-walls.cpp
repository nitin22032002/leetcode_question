//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    int shotestPath(vector<vector<int>> mat, int n, int m, int k) {
        queue<vector<int>> obj;
        vector<vector<int>> visited(n,vector<int>(m,-1));
        obj.push({0,0,k,0});
        int ans=-1;
        while(obj.size()!=0){
            auto top=obj.front();
            obj.pop();
            int i=top[0];
            int j=top[1];
            int k=top[2];
            int cost=top[3];
            if(i>=n or j>=m or i<0 or j<0 or (mat[i][j]==1 and k==0))
                continue;
            else if(i==n-1 and m-1==j)
                return cost;
            else{
                if(visited[i][j]>=k){
                    continue;
                }
                visited[i][j]=k;
                if(mat[i][j]==1)
                    k-=1;
                obj.push({i+1,j,k,cost+1});
                obj.push({i,j+1,k,cost+1});
                obj.push({i-1,j,k,cost+1});
                obj.push({i,j-1,k,cost+1});
            }
        }
        return -1;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m, k, x;
        
        cin>>n>>m>>k;
        vector<vector<int>> mat;
    
        for(int i=0; i<n; i++)
        {
            vector<int> row;
            for(int j=0; j<m; j++)
            {
                cin>>x;
                row.push_back(x);
            }
            mat.push_back(row);
        }

        Solution ob;
        cout<<ob.shotestPath(mat,n,m,k);
        cout<<"\n";
    }
    return 0;
}
// } Driver Code Ends