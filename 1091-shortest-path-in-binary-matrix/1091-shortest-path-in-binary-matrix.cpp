class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        queue<pair<int,pair<int,int>>> d;
        d.push({1,{0,0}});
        while(!d.empty()){
            auto top=d.front();
            d.pop();
            int cost=top.first;
            int i=top.second.first;
            int j=top.second.second;
            if(i==(grid.size()-1) && j==(grid[0].size()-1)){
                if(grid[i][j]==1){
                    return -1;
                }
                return cost;
            }
            else if(i>=grid.size() || j>=grid[0].size() || i<0 || j<0 || grid[i][j]==1)             {
                continue;
            }
            else{
                grid[i][j]=1;
                d.push({cost+1,{i+1,j}});
                d.push({cost+1,{i,j+1}});
                d.push({cost+1,{i-1,j}});
                d.push({cost+1,{i,j-1}});
                d.push({cost+1,{i+1,j+1}});
                d.push({cost+1,{i-1,j+1}});
                d.push({cost+1,{i-1,j-1}});
                d.push({cost+1,{i+1,j-1}});
            }
        }
        return -1;
    }
};