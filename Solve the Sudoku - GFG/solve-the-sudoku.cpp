//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
// UNASSIGNED is used for empty cells in sudoku grid 
#define UNASSIGNED 0  

// N is used for the size of Sudoku grid.  
// Size will be NxN  
#define N 9  


// } Driver Code Ends

class Solution {
public:
    bool SolveSudoku(int board[N][N]) {
        return get(board, 0, 0);
    }

private:
    bool get(int board[N][N], int i, int j) {
        if (i >= N) {
            return true;
        } else if (j >= N) {
            return get(board, i + 1, 0);
        } else if (board[i][j] != 0) {
            return get(board, i, j + 1);
        } else {
            for (int val = 1; val <= 9; val++) {
                if (validRC(board, i, j, val) && validBox(board, i, j, val)) {
                    board[i][j] = val;
                    if (get(board, i, j + 1)) {
                        return true;
                    }
                    board[i][j] = 0;
                }
            }
            return false;
        }
    }

    bool validRC(int board[N][N], int i, int j, int val) {
        bool d[9] = { false };
        for (int a = 0; a < N; a++) {
            if (board[i][a] != 0) {
                d[board[i][a] - 1] = true;
            }
        }
        if (d[val - 1]) {
            return false;
        }
        for (int a = 0; a < N; a++) {
            if (board[a][j] != 0) {
                d[board[a][j] - 1] = true;
            }
        }
        if (d[val - 1]) {
            return false;
        }
        return true;
    }

    bool validBox(int board[N][N], int i, int j, int val) {
        bool d[9] = { false };
        int col1 = (j / 3) * 3;
        int col2 = col1 + 3;
        int row1 = (i / 3) * 3;
        int row2 = row1 + 3;
        for (int x = row1; x < row2; x++) {
            for (int y = col1; y < col2; y++) {
                if (board[x][y] != 0) {
                    d[board[x][y] - 1] = true;
                }
            }
        }
        return !d[val - 1];
    }

public:
    void printGrid(int arr[N][N]) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << arr[i][j] << " ";
            }
        }
    }
};

//{ Driver Code Starts.

int main() {
	int t;
	cin>>t;
	while(t--)
	{
		int grid[N][N];
		
		for(int i=0;i<9;i++)
		    for(int j=0;j<9;j++)
		        cin>>grid[i][j];
		        
		Solution ob;
		
		if (ob.SolveSudoku(grid) == true)  
            ob.printGrid(grid);  
        else
            cout << "No solution exists";  
        
        cout<<endl;
	}
	
	return 0;
}
// } Driver Code Ends