class Solution {
public:
    int minimumObstacles(vector<vector<int>>& grid) {
        priority_queue<pair<int,pair<int,int>>,vector<pair<int,pair<int,int>>>,greater<pair<int,pair<int,int>>>> d;
        d.push({0,{0,0}});
        vector<vector<int>> dis(grid.size(),vector<int>(grid[0].size(),INT_MAX));
        dis[0][0]=0;
        int n=grid.size();
        int m=grid[0].size();
        while(d.size()>0){
            auto top=d.top();
            d.pop();
            auto index=top.second;
            if(index.first==n-1 && index.second==m-1){
                return top.first;
            }
            else{
                if(index.first+1<n && dis[index.first+1][index.second]>(top.first+grid[index.first+1][index.second])){
                    dis[index.first+1][index.second]=(top.first+grid[index.first+1][index.second]);
                    d.push({(top.first+grid[index.first+1][index.second]),{index.first+1,index.second}});
                }
                if(index.first-1>=0 && dis[index.first-1][index.second]>(top.first+grid[index.first-1][index.second])){
                    dis[index.first-1][index.second]=(top.first+grid[index.first-1][index.second]);
                    d.push({(top.first+grid[index.first-1][index.second]),{index.first-1,index.second}});
                }
                if(index.second+1<m && dis[index.first][index.second+1]>(top.first+grid[index.first][index.second+1])){
                    dis[index.first][index.second+1]=(top.first+grid[index.first][index.second+1]);
                    d.push({(top.first+grid[index.first][index.second+1]),{index.first,index.second+1}});
                }
                if(index.second-1>=0 && dis[index.first][index.second-1]>(top.first+grid[index.first][index.second-1])){
                    dis[index.first][index.second-1]=(top.first+grid[index.first][index.second-1]);
                    d.push({(top.first+grid[index.first][index.second-1]),{index.first,index.second-1}});
                }
            }
        }
        return 0;
    }
};