//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    long long jumpingNums(long long X) {
        vector<long long> jumpNumber={1,2,3,4,5,6,7,8,9};
        if(X<=10)
            return X;
        long long n=X;
        int c=0;
        while(n!=0){
            c+=1;
            n/=10;
        }
        long long ans=0;
        for(int i=0;i<c;i++){
            vector<long long> p;
            for(auto &item:jumpNumber){
                if(item%10==0)
                    p.push_back((item*10)+1);
                else if(item%10==9)
                    p.push_back((item*10)+8);
                else{
                    p.push_back((item*10)+((item%10)+1));
                    p.push_back((item*10)+((item%10)-1));
                }
                if(item<=X)
                    ans=max(ans,item);
            }
            for(int i=0;i<p.size();i++){
                if(i<jumpNumber.size()){
                    jumpNumber[i]=p[i];
                }
                else{
                    jumpNumber.push_back(p[i]);
                }
            }
        }
        for(auto &item:jumpNumber){
            if(item<=X)
                ans=max(ans,item);
        }
        return ans;
    }
};



//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        long long X;
        
        cin>>X;

        Solution ob;
        cout << ob.jumpingNums(X) << endl;
    }
    return 0;
}
// } Driver Code Ends