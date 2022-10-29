#User function Template for python3

class Solution:
    def displayContacts(self, n, contact, s):
        obj=Trie()
        for item in contact:
            obj.insert(item)
        return obj.search(s)
class Trie:
    def __init__(self):
        self.child=[None for _ in range(26)]
        self.word=None
    def insert(self,word):
        for item in word:
            j=ord(item)-97
            if(not self.child[j]):
                self.child[j]=Trie()
            self=self.child[j]
        self.word=word
    def search(self,word):
        ans=[]
        for item in word:
            j=ord(item)-97
            if(not self or not self.child[j]):
                ans.append("0")
                self=None
            else:
                self=self.child[j]
                res=self.findAll()
                # print(res)
                ans.append(res)
        return ans
    def findAll(self):
        ans=[]
        if(self.word):
            ans.append(self.word)
        for i in range(26):
            if(self.child[i]):
                ans.extend(self.child[i].findAll())
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends