class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        priority_queue<int,vector<int>,greater<int>> d;
        sort(intervals.begin(),intervals.end());
        int i=0;
        int ans=0;
        while(i<intervals.size()){
            if(d.size()==0 || d.top()>=intervals[i][0]){
                ans+=1;
                d.push(intervals[i][1]);
            }
            else{
                d.pop();
                d.push(intervals[i][1]);
                
            }
            i+=1;
        }
        return ans;
    }
};