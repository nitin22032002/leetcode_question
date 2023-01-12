//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
public:
    int minimizeSum(int N, vector<int> arr) {
        priority_queue<int,vector<int>,greater<int>> obj;
        for( auto &item : arr) 
            obj.push(item);
        int ans=0;
        while(obj.size()>1){
            int a1=obj.top();
            obj.pop();
            int a2=obj.top();
            obj.pop();
            ans+=(a1+a2);
            obj.push(a1+a2);
    }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
	int t;
    cin>>t;
    while(t--) {
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i = 0; i < n; i++)
            cin>>arr[i];
        Solution obj;
        cout << obj.minimizeSum(n, arr) << "\n";
    }
}
// } Driver Code Ends