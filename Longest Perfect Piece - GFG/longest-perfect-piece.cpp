//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int longestPerfectPiece(int arr[], int n) {
        multiset<int> d;
        int start=0,end=0,ans=0;
        while(end<n){
            if(d.size()>=1){
                auto mi=*d.begin();
                auto mx=(*(--d.end()));
                if(mx-mi<=1){
                    ans=max(ans,end-start);
                    d.insert(arr[end]);
                    end++;
                }
                else{
                    d.erase(d.find(arr[start]));
                    start++;
                }
                
            }
            else{
                d.insert(arr[end]);
                end+=1;
            }
        }
        while(start<n){
            if(d.size()>=1){
                auto mi=*d.begin();
                auto mx=(*(--d.end()));
                if(mx-mi<=1){
                    ans=max(ans,end-start);
                    break;
            }
            d.erase(d.find(arr[start]));
            start++;
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
        
        cin>>N;
        int arr[N];
        for(int i=0; i<N; i++)
            cin>>arr[i];

        Solution ob;
        cout << ob.longestPerfectPiece(arr,N) << endl;
    }
    return 0;
}
// } Driver Code Ends