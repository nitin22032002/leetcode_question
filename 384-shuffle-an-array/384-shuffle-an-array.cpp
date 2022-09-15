class Solution {
public:
    vector<int> nums,gen;
    Solution(vector<int>& nums) {
        this->nums=nums;
        this->gen=nums;
    }
    
    vector<int> reset() {
        return nums;
    }
    
    vector<int> shuffle() {
        next_permutation(gen.begin(),gen.end());
        return gen;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */