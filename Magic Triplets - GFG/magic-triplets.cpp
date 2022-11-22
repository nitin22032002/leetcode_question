//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	int countTriplets(vector<int>nums){
	    int ans=0;
	    for(int i=1;i<nums.size()-1;i++){
	        int j=0;
	        int r1=0;
	        while(j<i){
	            if(nums[j]<nums[i])
	                r1+=1;
	            j+=1;
	        }
	        j=i+1;
	        int r2=0;
	        while(j<nums.size()){
	            if(nums[j]>nums[i])
	               r2+=1;
                j+=1;
	        }
            ans+=(r1*r2);
	    }
	    return ans;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<int>nums(n);
		for(int i = 0; i < n; i++)cin >> nums[i];
		Solution ob;
		int ans = ob.countTriplets(nums);
		cout << ans << "\n";
	}  
	return 0;
}
// } Driver Code Ends