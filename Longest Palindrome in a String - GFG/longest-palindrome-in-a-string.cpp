//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    string longestPalin (string s) {
        int ans=0;
        int s1=0;
        int s2=s.size();
        for(int i=0;i<s.size();i++){
            int start=i-1;
            int end=i+1;
            int cost=1;
            while(start>=0 && end<s.size() && s[start]==s[end]){
                cost+=2;
                start-=1;
                end+=1;}
            if(ans<cost){
                ans=cost;
                s1=start+1;
                s2=end;
            }
            start=i;
            end=i+1;
            cost=0;
            while(start>=0 && end<s.size() && s[start]==s[end]){
                cost+=2;
                start-=1;
                end+=1;
            }
            if(ans<cost){
                ans=cost;
                s1=start+1;
                s2=end;
            }
        }
        string res;
        for(int i=s1;i<s2;i++){
            res.push_back(s[i]);
        }
        return res;
    }
};

//{ Driver Code Starts.

int main()
{
    int t; cin >> t;
    while (t--)
    {
        string S; cin >> S;
        
        Solution ob;
        cout << ob.longestPalin (S) << endl;
    }
}
// Contributed By: Pranay Bansal

// } Driver Code Ends