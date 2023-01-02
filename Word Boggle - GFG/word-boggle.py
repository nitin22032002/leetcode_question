#User function Template for python3

class Solution:
    def wordBoggle(self,board,dictionary):
        obj=Trie()
        for item in dictionary:
            obj.insert(item)
        ans=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                obj=self.get(board,i,j,obj,ans)
                if(not obj):return ans
        return ans
    def get(self,board,i,j,obj,ans):
        if(obj.isEnd):
            ans.append(obj.val)
            obj.isEnd=False
            if(len(obj.child)==0):
                return None
        if(i>=len(board) or j>=len(board[0]) or i<0 or j<0 or board[i][j]=="1" or not obj):
            return obj
        if(not obj.child.get(board[i][j],None)):
            return obj
        else:
            r=board[i][j]
            board[i][j]='1'
            obj.child[r]=obj.child[r] and self.get(board,i+1,j,obj.child[r],ans)
            obj.child[r]=obj.child[r] and self.get(board,i-1,j,obj.child[r],ans)
            obj.child[r]=obj.child[r] and self.get(board,i,j+1,obj.child[r],ans)
            obj.child[r]=obj.child[r] and self.get(board,i,j-1,obj.child[r],ans)
            obj.child[r]=obj.child[r] and self.get(board,i+1,j+1,obj.child[r],ans)
            obj.child[r]=obj.child[r] and self.get(board,i+1,j-1,obj.child[r],ans)
            obj.child[r]=obj.child[r] and self.get(board,i-1,j+1,obj.child[r],ans)
            obj.child[r]=obj.child[r] and self.get(board,i-1,j-1,obj.child[r],ans)
            board[i][j]=r
            if(not obj.child[r]):
                del obj.child[r]
            if(len(obj.child)==0):
                return None
            return obj
            
class Trie:
    def __init__(self):
        self.child={}
        self.val=None
        self.isEnd=False
    def insert(self,word):
        for item in word:
            if(not self.child.get(item,None)):
                self.child[item]=Trie()
            self=self.child[item]
            # self.val=item
        self.val=word
        # print(self.val)
        self.isEnd=True


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()                               # sorting output
        for i in found:
            print(i,end=' ')
        print()
# } Driver Code Ends