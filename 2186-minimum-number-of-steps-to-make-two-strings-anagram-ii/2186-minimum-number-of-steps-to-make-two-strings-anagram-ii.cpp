class Solution {
public:
    int minSteps(string s, string t) {
        vector<int> d1(26,0),d2(26,0);
        for(auto &val:s){
            d1[val-'a']+=1;
        }
        for(auto &val:t){
            d2[val-'a']+=1;
        }
        int cost=0;
        for(int i=0;i<26;i++){
                cost+=(d1[i]>d2[i]?d1[i]-d2[i]:d2[i]-d1[i]);
        }
        return cost;
    }
};