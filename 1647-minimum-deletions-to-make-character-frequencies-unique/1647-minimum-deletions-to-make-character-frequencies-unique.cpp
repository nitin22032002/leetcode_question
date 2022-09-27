class Solution {
public:
    int minDeletions(string s) {
        vector<int> fre(26,0);
        for(auto &val:s){
            fre[val-'a']+=1;
        }
        priority_queue<int> d;
        for(auto &val:fre){
            if(val!=0){
                // cout<<val<<endl;
                d.push(val);
            }
        }
        int ans=0;
        while(d.size()>1){
            int a=d.top();
            d.pop();
            int b=d.top();
            if(a==b and a!=0){
                d.push(a-1);
                ans++;
            }
            
        }
        return ans;
    }
};