class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Trie()
        for i in range(len(words)):
            root.insert(words[i])
        ans=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.get(board,i,j,root,ans)
        return ans
    def get(self,board,i,j,root,ans):
        # if(root):
        #     print(root.child,(i,j))
        if(root and root.word):
            ans.append(root.word)
            if(root.count==0):
                return None
            else:
                root.word=None
        if(i>=len(board) or j>=len(board[0]) or i<0 or j<0 or board[i][j]=="-" or not root or not root.child[ord(board[i][j])-97]):
            # print(board[i][j])
            return root
        else:
            t=ord(board[i][j])-97
            board[i][j]="-"
            a=self.get(board,i+1,j,root.child[t],ans)
            if(a!=root.child[t]):
                root.child[t]=a
                root.count-=1
            a=self.get(board,i-1,j,root.child[t],ans)
            if(a!=root.child[t]):
                root.child[t]=a
                root.count-=1
            a=self.get(board,i,j+1,root.child[t],ans)
            if(a!=root.child[t]):
                root.child[t]=a
                root.count-=1
            a=self.get(board,i,j-1,root.child[t],ans)
            if(a!=root.child[t]):
                root.child[t]=a
                root.count-=1
            board[i][j]=chr(t+97)
            if(root.count==0):
                return None
            return root
        
class Trie:
    def __init__(self):
        self.child=[None for _ in range(26)]
        self.word=None
        self.count=0
    def insert(self,word):
        for item in word:
            j=ord(item)-97
            if(not self.child[j]):
                self.child[j]=Trie()
                self.count+=1
            self=self.child[j]
        self.word=word
    
        