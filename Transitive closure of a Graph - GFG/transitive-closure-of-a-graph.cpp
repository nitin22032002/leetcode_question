//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// Back-end complete function Template for C++

class Solution {
public:
    std::vector<std::vector<int>> transitiveClosure(int N, std::vector<std::vector<int>> graph) {
        std::vector<std::vector<int>> ans(N, std::vector<int>(N, 0));
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                ans[i][j]=graph[i][j];
                if(i==j)
                    ans[i][j]=1;
            }
        }
        
        std::vector<bool> visited(N, false);
        
        for (int node = 0; node < N; node++) {
            if (!visited[node]) {
                get(graph, node, visited, ans);
            } else {
                for (int i = 0; i < N; i++) {
                    if (ans[node][i] != 0) {
                        for (int j = 0; j < N; j++) {
                            ans[node][j] = std::max(ans[node][j], ans[i][j]);
                        }
                    }
                }
            }
        }
        
        return ans;
    }
    
    void get(std::vector<std::vector<int>>& graph, int node, std::vector<bool>& visited, std::vector<std::vector<int>>& ans) {
        if (visited[node]) {
            return;
        }
        
        visited[node] = true;
        
        for (int i = 0; i < graph.size(); i++) {
            if (graph[node][i] != 0) {
                get(graph, i, visited, ans);
            }
        }
        
        for (int i = 0; i < graph.size(); i++) {
            if (ans[node][i] != 0) {
                for (int j = 0; j < graph.size(); j++) {
                    ans[node][j] = std::max(ans[node][j], ans[i][j]);
                }
            }
        }
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        vector<vector<int>> graph(N, vector<int>(N, -1));
        for(int i = 0;i < N;i++)
            for(int j=0;j<N;j++)
            cin>>graph[i][j];
        
        Solution ob;
        vector<vector<int>> ans = ob.transitiveClosure(N, graph);
        for(int i = 0;i < N;i++)
            {for(int j = 0;j < N;j++)
                cout<<ans[i][j]<<" ";
        cout<<"\n";}
    }
    return 0;
}
// } Driver Code Ends