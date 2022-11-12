//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
	public:
		int characterReplacement(string s, int k){
		    vector<int> d(26,0);
		    int i=0,j=0,count=0,m=0,ans=0;
		    while(j<s.size()){
		        int cost=count-m;
		        if(cost<=k){
		            ans=max(ans,j-i);
		            d[s[j]-'A']+=1;
		            count+=1;
		            m=max(m,d[s[j]-'A']);
		            j+=1;
		        }
		        else{
		            d[s[i]-'A']-=1;
		            count-=1;
		            m=*max_element(d.begin(),d.end());
		            i+=1;
		        }
		    }
		    while(i<s.size()){
		        int cost=count-m;
		        if(cost<=k){
		            ans=max(ans,j-i);
		            break;
		        }
		        else{
		            d[s[i]-'A']-=1;
		            count-=1;
		            m=*max_element(d.begin(),d.end());
		            i+=1;
		        }
		    }
		    return ans;
		}

};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string s;
		cin >> s;
		int k;
		cin >> k;
		Solution obj;
		int ans = obj.characterReplacement(s, k);
		cout << ans << "\n";
	}
	return 0;
}
// } Driver Code Ends