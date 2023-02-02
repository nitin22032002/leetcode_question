//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    pair<int,int> endPoints(vector<vector<int>> matrix){
        int i=0,j=0,r=0,s1=0,s2=1,m=matrix.size(),n=matrix[0].size();
        while(r<(m*n)){
            if(matrix[i][j]==0)
                {if(i+s1<0 or i+s1>=m or j+s2<0 or j+s2>=n)
                    return {i,j};
                i+=s1;
                j+=s2;
                r+=1;}
            else{
                if(s1==0 and s2==1)
                    {s1=1;
                    s2=0;}
                else if(s1==1 and s2==0)
                    {s2=-1;
                    s1=0;}
                else if(s2==-1 and s1==0)
                    {s2=0;
                    s1=-1;}
                else{
                    s1=0;
                    s2=1;}
                matrix[i][j]=0;
            }
        }
        return {-1,-1};
    }

};

//{ Driver Code Starts.


int main()
{
    int tc;
	scanf("%d", &tc);
	while(tc--){
		int row, col;
		scanf("%d", &row);
		scanf("%d", &col);
		vector<vector<int>> matrix(row , vector<int> (col));
	 
		for(int i = 0; i < row; i++){
			for(int j = 0; j < col; j++){
			    cin>>matrix[i][j];
			}
		}
		Solution obj;
		pair<int,int> p = obj.endPoints(matrix);
		
		cout << "(" << p.first << ", " << p.second << ")" << endl;
	}
	return 0;
}
// } Driver Code Ends