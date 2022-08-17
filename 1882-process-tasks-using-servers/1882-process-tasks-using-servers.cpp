class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> ava;
        priority_queue<pair<int,pair<int,int>>,vector<pair<int,pair<int,int>>>,greater<pair<int,pair<int,int>>>> unava;
        for(int i=0;i<servers.size();i++){
            ava.push({servers[i],i});
        }
        vector<int> ans;
        for(int i=0;i<tasks.size();i++){
            while(!unava.empty()){
                pair<int,pair<int,int>> t=unava.top();
                if(t.first<=i){
                    ava.push({(t.second).first,(t.second).second});
                    unava.pop();
                }
                else{
                    break;
                }
            }
            if(ava.empty()){
                pair<int,pair<int,int>> t=unava.top();
                ans.push_back((t.second).second);
                unava.pop();
                unava.push({t.first+tasks[i],t.second});
            }
            else{
            pair<int,int> t=ava.top();
            ans.push_back(t.second);
            unava.push({i+tasks[i],t});
            ava.pop();
            }
        }
        return ans;
        
    }
};