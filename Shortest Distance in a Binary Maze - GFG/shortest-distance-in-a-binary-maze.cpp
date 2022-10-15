//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int shortestPath(vector<vector<int>> &grid, pair<int, int> source,
                     pair<int, int> destination) {
        queue<pair<int,pair<int,int>>> d;
        d.push({0,source});
        vector<vector<bool>> visited(grid.size(),vector<bool>(grid[0].size(),false));
        while(!d.empty()){
            auto top=d.front();
            d.pop();
            int cost=top.first;
            int i=top.second.first;
            int j=top.second.second;
            if(i==destination.first && j==destination.second){
                return cost;
            }
            else if(i>=grid.size() || j>=grid[0].size() || i<0 || j<0 || visited[i][j] || grid[i][j]==0){
                continue;
            }
            else{
                visited[i][j]=true;
                d.push({cost+1,{i+1,j}});
                d.push({cost+1,{i,j+1}});
                d.push({cost+1,{i-1,j}});
                d.push({cost+1,{i,j-1}});
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
        int n, m;
        cin >> n >> m;
        vector<vector<int>> grid(n, vector<int>(m));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }

        pair<int, int> source, destination;
        cin >> source.first >> source.second;
        cin >> destination.first >> destination.second;
        Solution obj;
        cout << obj.shortestPath(grid, source, destination) << endl;
    }
}

// } Driver Code Ends