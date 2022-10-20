class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& tem) {
        stack<int> d;
        int n=tem.size();
        vector<int> ans(n,0);
        for(int i=0;i<n;i++){
            if(d.size()==0 || tem[d.top()]>=tem[i]){
                d.push(i);
            }
            else{
                while(d.size()!=0 && tem[d.top()]<tem[i]){
                    ans[d.top()]=(i-d.top());
                    d.pop();
                }
                d.push(i);
            }
        }
        return ans;
    }
};