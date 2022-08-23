# from numpy import array
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.get(board,i,j)
        # print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=="1"):
                    board[i][j]="O"
                else:
                    board[i][j]="X"
                    
    def get(self,arr,i,j):
        if(i<0 or i>=len(arr) or j<0 or j>=len(arr[0])):
            return False
        elif(arr[i][j]=="2" or arr[i][j]=="X" or arr[i][j]=="0"):
            return True
        elif(arr[i][j]=="1"):
            return False
        else:
            status=True
            arr[i][j]="0"
            status=(status and self.get(arr,i+1,j))
            status=(status and self.get(arr,i-1,j))
            status=(status and self.get(arr,i,j+1))
            status=(status and self.get(arr,i,j-1))
            if(status):
                arr[i][j]="2"
            else:
                arr[i][j]="2"
                self.setZero(arr,i,j)
            return status
    def setZero(self,arr,i,j):
        if(i<0 or i>=len(arr) or j<0 or j>=len(arr[0])):
            return False
        elif(arr[i][j]=="X" or arr[i][j]=="0"):
            return True
        elif(arr[i][j]=="1" or arr[i][j]=="O"):
            return False
        else:
            # print(arr[i][j])
            if(arr[i][j]=="2"):
                arr[i][j]="1"
            self.setZero(arr,i+1,j)
            self.setZero(arr,i-1,j)
            self.setZero(arr,i,j+1)
            self.setZero(arr,i,j-1)
            