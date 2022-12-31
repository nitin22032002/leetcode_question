//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    int minLaptops(int N, int start[], int end[]) {
       vector<pair<int,int>> arr;
        for(int i=0;i<N;i++){
            arr.push_back({start[i],end[i]});
        }
        sort(arr.begin(),arr.end());
        priority_queue<int,vector<int>,greater<int>> d;
        int ans=0;
        for(int i=0;i<N;i++){
            if(d.size()==0 or d.top()>arr[i].first){
                d.push(arr[i].second);
                ans++;
            }
            else{
            d.pop();
            d.push(arr[i].second);
            }
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
        int start[N], end[N];
        for(int i=0; i<N; i++)
            cin>>start[i];
        for(int i=0; i<N; i++)
            cin>>end[i];
            
        Solution ob;
        cout << ob.minLaptops(N, start, end) << endl;
    }
}
// } Driver Code Ends