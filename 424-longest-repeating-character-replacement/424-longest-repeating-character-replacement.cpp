class Solution {
public:
    int characterReplacement(string s, int k) {
        multiset<int> d;
        vector<int> val(26,0);
        int i=0;
        int j=0;
        int count=0;
        int ans=0;
        while(i<s.size()){
            if(d.size()==0){
                count+=1;
                val[s[i]-'A']+=1;
                d.insert(-1);
                i+=1;
            }
            else{
                int v=-(*d.begin());
                // cout<<v<<endl;
                if(count-v<=k){
                    ans=max(ans,(i-j));
                    if(val[s[i]-'A']!=0)
                        d.erase(d.find(-val[s[i]-'A']));
                    val[s[i]-'A']+=1;
                    d.insert(-val[s[i]-'A']);
                    count+=1;
                    i+=1;
                }
                else{
                    d.erase(d.find(-val[s[j]-'A']));
                    val[s[j]-'A']-=1;
                    d.insert(-val[s[j]-'A']);
                    count-=1;
                    j+=1;
                }
            }
        }
        while(j<s.size()){
            int v=-(*d.begin());
                if(count-v<=k){
                    ans=max(ans,(i-j));
                    
                }
            d.erase(d.find(-val[s[j]-'A']));
                    val[s[j]-'A']-=1;
                    d.insert(-val[s[j]-'A']);
                    count-=1;
                    j+=1;
        }
        return ans;
    }
};