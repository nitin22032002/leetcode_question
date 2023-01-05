#User function Template for python3


class Solution():
    def longestString(self, arr, n):
        obj=Trie()
        for item in arr:
            obj.insert(item)
        ans=""
        arr.sort()
        for item in arr:
            if(obj.search(item)):
                if(len(item)>len(ans)):
                    ans=item
        return ans
class Trie:
    def __init__(self):
        self.child=[None for _ in range(26)]
        self.isEnd=False
    def insert(self,word):
        for item in word:
            j=ord(item)-97
            if(not self.child[j]):
                self.child[j]=Trie()
            self=self.child[j]
        self.isEnd=True
    def search(self,word):
        for item in word:
            j=ord(item)-97
            self=self.child[j]
            if(not self.isEnd):
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends