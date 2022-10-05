class Solution {
public:
    int minRemove(string &s){
        stack<char> d;
        int count=0;
        for(auto &ch:s){
            if(ch=='('){
                d.push(ch);
            }
            else if(ch==')'){
                if(d.size()==0){
                    count++;
                }
                else{
                    d.pop();
                }
            }
        }
        count+=d.size();
        return count;
    }
    bool valid(string &s){
        stack<char> d;
        for(auto &ch:s){
            if(ch=='('){
                d.push(ch);
            }
            else if(ch==')'){
                if(d.size()==0){
                    return false;
                }
                else{
                    d.pop();
                }
            }
        }
        return d.empty();
    }
    void solve(string &s,int mn,int i,set<string> &ans){
        // cout<<mn<<","<<i<<endl;
        if(mn==0){
            // cout<<s<<endl;
            if(valid(s)){
                ans.insert(s);
            }
            return ;
        }
        else if(i>=s.size()){
            return ;
        }
        else{
            if(s[i]=='(' || s[i]==')'){
                string s1=s.substr(0,i)+s.substr(i+1,(s.size()-i));
                solve(s1,mn-1,i,ans);
            }
                solve(s,mn,i+1,ans);
        }
    }
    vector<string> removeInvalidParentheses(string s) {
        int mn=minRemove(s);
        set<string> ans;
        solve(s,mn,0,ans);
        vector<string> result;
        for(auto it=ans.begin();it!=ans.end();it++){
            result.push_back(*it);
        }
        return result;
    }
};