//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    vector<int> maxCombinations(int N, int k, vector<int> &A, vector<int> &B) {
        sort(A.begin(),A.end());
        sort(B.begin(),B.end());
        reverse(A.begin(),A.end());
        reverse(B.begin(),B.end());
        vector<int> ans;
        priority_queue<vector<int>> obj;
        for(int i=0;i<N;i++)
            obj.push({(A[i]+B[0]),0,i});
        while(k!=0 and !obj.empty()){
            auto val=obj.top();
            obj.pop();
            ans.push_back(val[0]);
            if(val[1]+1<N)
                obj.push({(B[val[1]+1]+A[val[2]]),val[1]+1,val[2]});
            k-=1;
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K;
        cin >> N >> K;

        vector<int> A(N), B(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        for (int i = 0; i < N; i++) {
            cin >> B[i];
        }
        Solution obj;
        vector<int> ans = obj.maxCombinations(N, K, A, B);
        for (auto &it : ans) cout << it << ' ';
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends