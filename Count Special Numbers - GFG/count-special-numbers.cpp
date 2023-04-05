//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int countSpecialNumbers(int N, vector<int> arr) {
        int ans = 0;
unordered_map<int, int> d;
for(int i = 0; i < N; i++) {
    int item = arr[i];
    if(d.find(item) != d.end()) d[item]++;
    else d[item] = 1;
}
if(d.find(1) != d.end()) {
    if(d[1] > 1) return N;
    return N-1;
}
for(int i = 0; i < N; i++) {
    int item = arr[i];
    for(int j = 1; j <= item; j++) {
        if(item % j == 0) {
            if(item == j && d[j] > 1) {
                ans++;
                break;
            }
            else if(d.find(j) != d.end() && item != j) {
                ans++;
                break;
            }
        }
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
        vector<int> arr(N);
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }

        Solution ob;
        cout << ob.countSpecialNumbers(N, arr) << endl;
    }
    return 0;
}
// } Driver Code Ends