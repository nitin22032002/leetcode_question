class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        multiset<int> d;
        int k=indexDiff<nums.size()-1?indexDiff:nums.size()-1;
        for(int i=0;i<=k;i++){
            d.insert(nums[i]);
        }
        int i=0;
        int j=indexDiff+1;
        while(i<nums.size()){
            d.erase(d.find(nums[i])); 
            auto itr=d.lower_bound(valueDiff+nums[i]);
            // cout<<*itr<<endl;
            if(*itr==(valueDiff+nums[i])){
                return true;
            }
            else if(itr!=d.begin() && *(--itr)>=(nums[i]-valueDiff)){
                return true;
            }
            else{
                if(j<nums.size()){
                    d.insert(nums[j]);
                    j+=1;
                }
                i+=1;
            }
        }
        return false;
    }
};