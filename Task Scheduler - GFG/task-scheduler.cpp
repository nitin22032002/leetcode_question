//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
public:
    int leastInterval(int N, int k, std::vector<char>& tasks) {
        std::unordered_map<char, int> count;
        for (char task : tasks) {
            count[task]++;
        }

        std::priority_queue<int,vector<int>,greater<int>> pq;
        for (auto& pair : count) {
            pq.push(pair.second);
        }

        int ans = 0;
        k++;
        int lastIdle = 0;
        while (!pq.empty()) {
            if (pq.size() > k) {
                std::vector<int> arr;
                while (pq.size() > k) {
                    arr.push_back(pq.top());
                    pq.pop();
                }
                int ele = pq.top();
                pq.pop();
                pq.push(ele);
                int x = ele - arr.back() + 1;
                ans += x * k;
                while (!pq.empty()) {
                    arr.push_back(pq.top() - x);
                    pq.pop();
                }
                for (int item : arr) {
                    if (item != 0) {
                        pq.push(item);
                    }
                }
            } else {
                lastIdle = k - pq.size();
                int x = pq.top();
                pq.pop();
                ans += x * k;
                std::vector<int> arr;
                while (!pq.empty()) {
                    arr.push_back(pq.top() - x);
                    pq.pop();
                }
                for (int item : arr) {
                    if (item != 0) {
                        pq.push(item);
                    }
                }
            }
        }
        return ans - lastIdle;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K;
        cin >> N >> K;

        vector<char> tasks(N);
        for (int i = 0; i < N; i++) cin >> tasks[i];

        Solution obj;
        cout << obj.leastInterval(N, K, tasks) << endl;
    }
    return 0;
}
// } Driver Code Ends