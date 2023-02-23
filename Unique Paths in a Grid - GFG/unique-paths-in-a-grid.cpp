//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
public:
    int uniquePaths(int n, int m, std::vector<std::vector<int>>& grid) {
        dp = std::vector<std::vector<int>>(n, std::vector<int>(m, -1));
        mod = 1e9 + 7;
        return get(grid, 0, 0);
    }
    
private:
    std::vector<std::vector<int>> dp;
    int mod;
    
    int get(std::vector<std::vector<int>>& grid, int i, int j) {
        if (i == grid.size() - 1 && j == grid[0].size() - 1 && grid[i][j] != 0) {
            return 1;
        }
        else if (i >= grid.size() || j >= grid[0].size() || grid[i][j] == 0) {
            return 0;
        }
        else if (dp[i][j] == -1) {
            dp[i][j] = (get(grid, i+1, j) + get(grid, i, j+1)) % mod;
        }
        return dp[i][j];
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n,m,x;
        cin>>n>>m;
        
        vector<vector<int>> grid(n,vector<int>(m));
        
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                cin>>grid[i][j];
            }
        }

        Solution ob;
        cout << ob.uniquePaths(n,m,grid) << endl;
    }
    return 0;
}
// } Driver Code Ends