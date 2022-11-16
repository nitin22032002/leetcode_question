//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int findMin(vector<int> &arr){
        int ans=INT_MAX;
        for(auto &val:arr){
            if(val!=0)
                ans=min(ans,val);
        }
        return ans;
    }
    int beautySum(string s) {
       
       int ans=0;
       for(int i=0;i<s.size();i++){
           vector<int> r(26,0);
           int mi=INT_MAX;
           int ma=INT_MIN;
           for(int j=i;j<s.size();j++){
               
               r[s[j]-97]+=1;
               ma=max(ma,r[s[j]-97]);
               if(mi==r[s[j]-97]-1){
                   mi=findMin(r);
               }
               else{
                   mi=min(mi,r[s[j]-97]);
               }
               ans+=(ma-mi);
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
        string s;
        cin >> s;
        Solution obj;
        cout << obj.beautySum(s) << endl;
    }
    return 0;
}
// } Driver Code Ends