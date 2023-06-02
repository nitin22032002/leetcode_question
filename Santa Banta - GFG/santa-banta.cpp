//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
public:
    vector<int> primes;

    void precompute() {
        int size = 1200001;
        vector<bool> arr(size, true);
        arr[0] = false;
        arr[1] = false;

        int i = 2;
        while (i * i <= size) {
            if (arr[i]) {
                for (int j = i * i; j < size; j += i) {
                    arr[j] = false;
                }
            }
            i++;
        }

        for (int i = 0; i < size; i++) {
            if (arr[i]) {
                primes.push_back(i);
            }
        }
    }

    int helpSanta(int n, int m, vector<vector<int>>& g) {
        if (m == 0) {
            return -1;
        }

        int ans = 0;
        vector<bool> visited(n, false);

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                ans = max(ans, get(g, i, visited));
            }
        }

        return primes[ans - 1];
    }

    int get(vector<vector<int>>& graph, int node, vector<bool>& visited) {
        if (visited[node]) {
            return 0;
        }

        visited[node] = true;
        int ans = 1;

        for (int item : graph[node + 1]) {
            if (item <= visited.size()) {
                ans += get(graph, item - 1, visited);
            }
        }

        return ans;
    }
};


//{ Driver Code Starts.

int main(){
	int t;cin>>t;
	Solution ob;
	ob.precompute();
	while(t--){
        int n,e,u,v;
        cin>>n>>e;
        vector<vector<int>> g(n+10);
        
		for(int i = 0; i < e; i++)
		{
			cin>>u>>v;
			g[u].push_back(v);
			g[v].push_back(u);
		}
		cout << ob.helpSanta(n, e, g) << endl;
		
	}
}



// } Driver Code Ends