//{ Driver Code Starts
#include<bits/stdc++.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

// } Driver Code Ends
/* You are required to complete the function below
*  arr[]: input array
*  n: size of array
*/
class Solution{
  public:
    //Function to find triplets with zero sum.
    bool findTriplets(int arr[], int n)
    { 
        sort(arr, arr+n);
    
    for (int i = 0; i < n; i++) {
        int k = 0;
        int j = n - 1;
        while (k < j) {
            if (k == i) {
                k++;
                continue;
            }
            else if (j == i) {
                j--;
                continue;
            }
            
            int s = arr[k] + arr[j];
            if (s == -arr[i]) {
                return true;
            }
            else if (s > -arr[i]) {
                j--;
            }
            else {
                k++;
            }
        }
    }
    
    return false;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
	cin>>t;
	while(t--){
    	int n;
    	cin>>n;
    	int arr[n]={0};
    	for(int i=0;i<n;i++)
    		cin>>arr[i];
    	Solution obj;
        if(obj.findTriplets(arr, n))
            cout<<"1"<<endl;
        else 
            cout<<"0"<<endl;
	}
    return 0;
}
// } Driver Code Ends