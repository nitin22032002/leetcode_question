//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
        vector<int> updateQuery(int N, int Q, vector<vector<int>>& U) {
    vector<vector<vector<int>>> updateArr(N, vector<vector<int>>(2, vector<int>(32)));
    for(auto u : U) {
        int l = u[0]-1, r = u[1]-1, x = u[2];
        for(int i=0; i<32; i++) {
            if(((x>>i)&1) != 0) {
                updateArr[l][0][i] += 1;
                updateArr[r][1][i] += 1;
            }
        }
    }
    vector<int> count(32,0);
    vector<int> ans;
    for(int i=0; i<N; i++) {
        int bit = 0;
        for(int j=0; j<32; j++) {
            count[j] += updateArr[i][0][j];
            if(count[j] >= 1) {
                bit |= (1<<j);
            }
            count[j] -= updateArr[i][1][j];
        }
        ans.push_back(bit);
    }
    return ans;
}

};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,q;
        cin>>n>>q;
        vector <vector <int>> u(q,vector <int>(3));
        for(int i=0;i<q;i++)
            cin>>u[i][0]>>u[i][1]>>u[i][2];
        Solution a;
        vector <int> ans=a.updateQuery(n,q,u);//<<endl;
        for(auto j:ans)
        {
            cout<<j<<" ";
        }
        cout<<endl;
    }
    return 0;
}
// } Driver Code Ends