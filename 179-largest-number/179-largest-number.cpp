class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> d;
        for(auto &val:nums){
            long long int a=val;
            string s;
            while(a){ 
                char t=(a%10)+'0';
                s.push_back(t);
                a/=10;
            }
            reverse(s.begin(),s.end());
            if(val==0){
                s.push_back('0');
            }
            d.push_back(s);
        }
        sort(d.begin(),d.end(),greater<string>());
        for(int i=0;i<d.size();i++){
            for(int j=i+1;j<d.size();j++){
                if((d[i]+d[j])<(d[j]+d[i])){
                    string t=d[i];
                    d[i]=d[j];
                    d[j]=t;
                }
            }
        }
        string ans="";
        bool isInt=false;
        for(int i=0;i<d.size();i++){
            if(d[i]=="0" && !isInt){
                continue;
            }
            isInt=true;
            ans+=d[i];
        }
        if(ans.size()==0){
            return "0";
        }
        return ans;
    }
    
};