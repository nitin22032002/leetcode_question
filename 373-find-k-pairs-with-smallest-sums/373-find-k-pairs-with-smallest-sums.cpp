class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue<pair<int,pair<int,int>>> d;
        for(int i=0;i<nums1.size();i++){
            d.push({-(nums1[i]+nums2[0]),{i,0}});
        }
        vector<vector<int>> result;
        while(k>0 && d.size()>0){
            auto pit= d.top();
            vector<int> tem;
            auto it=pit.second;
            tem.push_back(nums1[it.first]);
            tem.push_back(nums2[it.second]);
            result.push_back(tem);
            d.pop();
            if(it.second+1<nums2.size()){
                d.push({-(nums1[it.first]+nums2[it.second+1]),{it.first,it.second+1}});
            }
            k-=1;
        }
        return result;
    }
};