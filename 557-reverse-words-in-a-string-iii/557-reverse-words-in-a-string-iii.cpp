class Solution {
public:
    string reverseWords(string s) {
        int i=0;
        while(i<s.size()){
            int j=i;
            while(j<s.size() && s[j]!=' '){
                j+=1;
            }
            int t=j-1;
            while(i<t){
                char a=s[i];
                s[i]=s[t];
                s[t]=a;
                i+=1;
                t-=1;
            }
            while(j<s.size() && s[j]==' '){
                j+=1;
            }
            i=j;
        }
        return s;
    }
};