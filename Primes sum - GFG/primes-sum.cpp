//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
public:
    string isSumOfTwo(int N){
        for(int i=2;i<=N/2;i++){
            if(isPrime(i) && isPrime(N-i)){
                return "Yes";
            }
        }
        return "No";
    }
    bool isPrime(int n){
        if(n<2){
            return false;
        }
        int i=2;
        while(i*i<=n){
            if(n%i==0){
                return false;
            }
            i+=1;
        }
        return true;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        Solution ob;
        cout << ob.isSumOfTwo(N) << endl;
    }
    return 0;
}

// } Driver Code Ends