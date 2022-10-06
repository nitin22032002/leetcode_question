class AllOne {
public:
    unordered_map<int,unordered_set<string>> dp;
    unordered_map<string,int> d;
    int maxP;
    int minP;
    AllOne() {
        maxP=0;
        minP=0;
    }
    
    void inc(string key) {
        int freq=d[key];
        if(freq!=0){
            dp[freq].erase(key);
            if(freq==minP && dp[freq].size()==0){
                minP=freq+1;
            }
        }
        d[key]+=1;
        if(minP==0){
            minP=1;
        }
        else{
            minP=min(minP,d[key]);
        }
        maxP=max(maxP,d[key]);
        dp[d[key]].insert(key);
        // cout<<minP<<","<<maxP<<endl;
    }
    
    void dec(string key) {
        int freq=d[key];
            dp[freq].erase(key);
            if(dp[freq].size()==0){
                if(maxP==freq){
                    maxP-=1;
                }
                if(minP==freq){
                    if(maxP==0){
                        minP=0;
                    }
                    else if(freq!=1){
                        minP-=1;
                    }
                    else{
                        while(dp[minP].size()==0){
                            minP+=1;
                        }
                    }
                }
            }
        else{
            if(minP==freq && freq!=1){
                minP-=1;
            }
        }
        d[key]-=1;
        dp[d[key]].insert(key);
        // cout<<minP<<","<<maxP<<endl;
    }
    
    string getMaxKey() {
        if(maxP==0){
            return "";
        }
        else{
            return *(dp[maxP].begin());
        }
    }
    
    string getMinKey() {
        if(minP==0){
            return "";
        }
        else{
            return *(dp[minP].begin());
        }
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */