//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct val{
	int first;
	int second;
};


// } Driver Code Ends
/*
The structure to use is as follows
struct val{
	int first;
	int second;
};*/

class Solution{
public:
    /*You are required to complete this method*/
    bool static compare(struct val &v1,struct val &v2){
        if(v1.second<v2.second)
            return true;
        else if(v1.second==v2.second)
            return v1.first<v2.first;
        return false;
    }
    int maxChainLen(struct val p[],int n){
        sort(p,p+n,compare);
        // cout<<p[0].first<<","<<p[0].second<<endl;
        vector<int> arr;
        // cout<<p[0].first<<endl;
        for(int i=0;i<n;i++){
            auto item=p[i];
            if(arr.size()==0 or arr[arr.size()-1]<item.first)
                arr.push_back(item.second);
            else if(arr[arr.size()-1]>item.second){
                auto j=lower_bound(arr.begin(),arr.end(),item.second)-arr.begin();
                arr[j]=item.second;
            }
        }
        return arr.size();
    }
};

//{ Driver Code Starts.

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		val p[n];
		for(int i=0;i<n;i++)
		{
			cin>>p[i].first>>p[i].second;
		}
		Solution ob;
		cout<<ob.maxChainLen(p,n)<<endl;
	}
	return 0;
}
// } Driver Code Ends