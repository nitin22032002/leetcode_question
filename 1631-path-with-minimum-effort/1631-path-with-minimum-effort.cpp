class Solution {
public:
    int compute(vector<vector<int>>& grid,int i1,int j1,int i2,int j2,int curr){
        return max(abs(grid[i1][j1]-grid[i2][j2]),curr);
    }
    int minimumEffortPath(vector<vector<int>>& grid) {
       priority_queue<pair<int,pair<int,int>>,vector<pair<int,pair<int,int>>>,greater<pair<int,pair<int,int>>>> d;
        d.push({0,{0,0}});
        vector<vector<int>> dis(grid.size(),vector<int>(grid[0].size(),INT_MAX));
        dis[0][0]=0;
        int n=grid.size();
        int effort=INT_MAX;
        int m=grid[0].size();
        while(d.size()>0){
            auto top=d.top();
            d.pop();
            auto index=top.second;
            if(index.first==n-1 && index.second==m-1){
                effort=min(effort,top.first);
            }
            else{
                if(index.first+1<n){
                    int cost=compute(grid,index.first,index.second,index.first+1,index.second,top.first);
                    if(cost<dis[index.first+1][index.second]){
                        
                    dis[index.first+1][index.second]=cost;
                    d.push({cost,{index.first+1,index.second}});
                    }
                }
                if(index.first-1>=0){
                    int cost=compute(grid,index.first,index.second,index.first-1,index.second,top.first);
                    if(cost<dis[index.first-1][index.second]){
                        
                    dis[index.first-1][index.second]=cost;
                    d.push({cost,{index.first-1,index.second}});
                    }
                }
                if(index.second+1<m){
                    int cost=compute(grid,index.first,index.second,index.first,index.second+1,top.first);
                    if(cost<dis[index.first][index.second+1]){
                        
                    dis[index.first][index.second+1]=cost;
                    d.push({cost,{index.first,index.second+1}});
                    }
                }
                if(index.second-1>=0){
                    int cost=compute(grid,index.first,index.second,index.first,index.second-1,top.first);
                    if(cost<dis[index.first][index.second-1]){
                        
                    dis[index.first][index.second-1]=cost;
                    d.push({cost,{index.first,index.second-1}});
                    }
                }
            }
        }
        return effort; 
    }
};