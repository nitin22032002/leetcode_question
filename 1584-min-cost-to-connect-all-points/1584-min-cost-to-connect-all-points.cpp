class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> d;
        d.push({0,0});
        vector<bool> visited(points.size(),false);
        int cost=0;
        int n=points.size();
        int i=0;
        while(!d.empty() && n>0){
            auto top=d.top();
            d.pop();
            if(visited[top.second]){
                continue;
            }
            cost+=top.first;
            visited[top.second]=true;
            n-=1;
            i=top.second;
            for(int j=0;j<points.size();j++){
                if(!visited[j]){
                    d.push({abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),j});
                }
            }
        }
        return cost;
    }
};