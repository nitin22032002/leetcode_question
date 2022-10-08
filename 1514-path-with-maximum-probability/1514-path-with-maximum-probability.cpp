class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        vector<vector<pair<int,float>>> graph(n);
        for(int i=0;i<edges.size();i++){
            graph[edges[i][0]].push_back({edges[i][1],succProb[i]});
            graph[edges[i][1]].push_back({edges[i][0],succProb[i]});
        }
        priority_queue<pair<float,int>> d;
        d.push({1,start});
        vector<float> dis(n,0);
        dis[start]=1;
        while(!d.empty()){
            auto top=d.top();
            d.pop();
            for(auto &val:graph[top.second]){
                if(dis[val.first]<top.first*val.second){
                    dis[val.first]=(top.first*val.second);
                    d.push({dis[val.first],val.first});
                }
            }
        }
        return dis[end];
    }
};