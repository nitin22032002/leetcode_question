//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++
class Solution{
public:


vector<vector<int>> chefAndWells(int n, int m, vector<vector<char>>& c) {
    queue<pair<int,int>> obj;
    vector<vector<int>> ans(n,vector<int>(m,1e9));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (c[i][j]== 'W') {
                obj.push({i, j});
                ans[i][j]=0;
            }
        }
    }
    vector<int> r1={1,-1,0,0},r2={0,0,1,-1};
    while (!obj.empty()) {
        auto p=obj.front();obj.pop();
        int i = p.first;
        int j = p.second;
        for(int k=0;k<4;k++){
            int i1=i+r1[k];
            int j1=j+r2[k];
            if(i1>=0 && i1<n && j1>=0 && j1<m && c[i1][j1]!='N' && ans[i1][j1]>(ans[i][j]+1)){
                ans[i1][j1]=ans[i][j]+1;
                obj.push({i1,j1});
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (ans[i][j]==1e9 && c[i][j]=='H') {
                    ans[i][j]=-1;
            }
            else if(c[i][j]!='H'){
                ans[i][j]=0;
            }
            else{
                ans[i][j]*=2;
            }
        }
    }
    return ans;
}

};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        vector<vector<char>> c(n,vector<char>(m));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>c[i][j];
            }
        }
        Solution ob;
        vector<vector<int>> res=ob.chefAndWells(n,m,c);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cout<<res[i][j]<<" ";
            }
            cout<<endl;
        }
    }
}
// } Driver Code Ends