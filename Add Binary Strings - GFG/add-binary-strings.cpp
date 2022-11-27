//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	
	string addBinary(string A, string B)
	{
        int carray=0;
        string ans;
        int i=A.size()-1;
        int j=B.size()-1;
        while(i>=0 && j>=0){
            if(A[i]=='1' and B[j]=='1'){
                if(carray==1)
                    ans.push_back('1');
                else
                    ans.push_back('0');
                carray=1;
            }
            else if(A[i]=='0' and B[j]=='0'){
                if(carray==1)
                    ans.push_back('1');
                else
                    ans.push_back('0');
                carray=0;
            }
            else{
                if(carray!=1)
                    ans.push_back('1');
                else
                    ans.push_back('0');
            }
            i-=1;
            j-=1;
        }
        while(i>=0){
               if(A[i]=='1'){
                   if(carray!=1)
                       ans.push_back('1');
                   else
                       ans.push_back('0');
               }
               else{
                   if(carray==1)
                       ans.push_back('1');
                   else
                       ans.push_back('0');
                   carray=0;
               }
               i-=1;
        }
        while(j>=0){
               if(B[j]=='1'){
                   if(carray!=1)
                       ans.push_back('1');
                   else
                       ans.push_back('0');
               }
               else{
                   if(carray==1)
                       ans.push_back('1');
                   else
                       ans.push_back('0');
                   carray=0;
               }
               j-=1;
        }
        if(carray)
            ans.push_back('1');
        int l=ans.length()-1;
        while(l>=0 and ans[l]=='0'){
            ans.pop_back();
            l-=1;
        }
        reverse(ans.begin(),ans.end());
        return ans;
	}
};

//{ Driver Code Starts.

int main()
{
	int t; cin >> t;
	while (t--)
	{
		string A, B; cin >> A >> B;
		Solution ob;
		cout << ob.addBinary (A, B);
		cout << "\n";
	}
}

// Contributed By: Pranay Bansal

// } Driver Code Ends