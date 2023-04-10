//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int maxIntersections(vector<vector<int>> lines, int N) {
        multiset<int> d;
        sort(lines.begin(),lines.end());
        int ans=0;
        for(int i=0;i<N;i++){
            d.insert(lines[i][1]);
            while(d.size()>0 && (*d.begin())<lines[i][0]){
                d.erase(d.begin());
            }
            int sz=d.size();
            ans=max(ans,sz);
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        vector<vector<int>> mat(N, vector<int>(2));
        for (int j = 0; j < 2; j++) {
            for (int i = 0; i < N; i++) {
                cin >> mat[i][j];
            }
        }
        Solution obj;
        cout << obj.maxIntersections(mat, N) << endl;
    }
}
// } Driver Code Ends