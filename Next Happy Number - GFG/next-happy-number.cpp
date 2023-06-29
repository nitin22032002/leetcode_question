//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public:
    int nextHappy(int N){
        std::unordered_set<int> not_happy;
        std::unordered_set<int> happy{1};
        int i = 1;

        while (true) {
            bool s = get(i, not_happy, happy);
            if (i > N && s) {
                return i;
            }
            i++;
        }
    }

private:
    bool get(int i, std::unordered_set<int>& not_happy, std::unordered_set<int>& happy) {
        if (happy.count(i)) {
            return true;
        } else if (not_happy.count(i)) {
            return false;
        } else {
            not_happy.insert(i);
            int t = 0;
            int r = i;
            while (i != 0) {
                t += std::pow(i % 10, 2);
                i /= 10;
            }
            bool s = get(t, not_happy, happy);
            if (s) {
                not_happy.erase(r);
                happy.insert(r);
            }
            return s;
        }
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.nextHappy(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends