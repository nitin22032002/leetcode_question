//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
public:
	int isNegativeWeightCycle(int n, vector<vector<int>>edges){
	    vector<long long int> dis(n,INT_MAX);
	    dis[0]=0;
	    for(int i=0;i<n-1;i++){
	        for(auto &val:edges){
	            dis[val[1]]=min(dis[val[1]],dis[val[0]]+val[2]);
	        }
	    }
	    for(auto &val:edges){
	            if(dis[val[1]]>((dis[val[0]]+val[2]))){
	                return true;
	            }
	        }
	        return false;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>edges;
		for(int i = 0; i < m; i++){
			int x, y, z;
			cin >> x >> y >> z;
			edges.push_back({x,y,z});
		}
		Solution obj;
		int ans = obj.isNegativeWeightCycle(n, edges);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends