class Solution {
public:
    string convert(string s, int numRows) {
        string ans;
        if(numRows<2){
            return s;
        }
        for(int i=0;i<numRows;i++){
            int k=i;
            int g=1;
            for(int j=0;j<s.size() && k<s.size();j++){
                if(g!=0)
                    ans.push_back(s[k]);
                // cout<<s[k]<<","<<k<<endl;
                if(j%2==0){
                    g=2*(numRows-i-1);
                    k+=g;
                }
                else{
                    g=2*i;
                    k+=g;
                }
            }
        }
        return ans;
    }
};