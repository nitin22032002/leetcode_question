#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        obj1=Trie()
        obj2=Trie()
        for item in s1:
            obj1.insert(item)
            obj2.insert(item[::-1])
        ans=0
        for item in s2:
            if(obj1.find(item) or obj2.find(item[::-1])):
                ans+=1
        return ans
class Trie:
    def __init__(self):
        self.child={}
    def insert(self,word):
        d=self.child
        for item in word:
            if(item not in d):
                d[item]={}
            d=d[item]
    def find(self,word):
        d=self.child
        for item in word:
            if(item not in d):
                return False
            d=d[item]
        return True

#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        s1 = list(map(str, input().split()))
        s2 = list(map(str, input().split()))
        obj=Solution()
        print(obj.prefixSuffixString(s1, s2))
# } Driver Code Ends