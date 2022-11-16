//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int beautySum(string s) {
       
       int ans=0;
       for(int i=0;i<s.size();i++){
           vector<int> r(26,0);
           multiset<int> d;
           for(int j=i;j<s.size();j++){
               if(r[s[j]-97]!=0){
                   d.erase(d.find(r[s[j]-97]));
               }
               r[s[j]-97]+=1;
               d.insert(r[s[j]-97]);
               ans+=((*(--d.end()))-(*d.begin()));
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