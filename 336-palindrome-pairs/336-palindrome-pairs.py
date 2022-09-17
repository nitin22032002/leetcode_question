class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        obj=Trie()
        for i in range(len(words)):
            obj.insert(words[i],i)
        ans=[]
        for i in range(len(words)):
            val=obj.search(words[i][::-1],i)
            ans.extend(val)
                    
        return ans
        
    
class Trie:
    def __init__(self,isEnd=False,index=-1,val=""):
        self.child=[None for _ in range(26)]
        self.isEnd=isEnd
        self.index=index
        self.val=val
    def insert(self,word,index):
        for item in word:
            j=ord(item)-97
            if(not self.child[j]):
                self.child[j]=Trie(val=item)
            self=self.child[j]
        self.isEnd=True
        self.index=index
    def search(self,word,ind):
        i=0
        index=-1
        a=[]
        while(i<len(word) and self):
            item=word[i]
            j=ord(item)-97
            if(not self.child[j]):
                if(not self.isEnd):
                    return a
                t=len(word)-1
                while(i<t):
                    if(word[i]!=word[t]):
                        return a
                    i+=1
                    t-=1
                if(self.index!=ind):
                    a.append([self.index,ind])
                    return a
            if(self.isEnd):
                # print(self.val,word,i)
                k=i
                t=len(word)-1
                while(k<t):
                    if(word[k]!=word[t]):
                        break
                    k+=1
                    t-=1
                # print((k,t,self.index,ind))
                if(k>=t and self.index!=ind):
                    a.append([self.index,ind])
                # print(a)
            self=self.child[j]
            i+=1
        if(not self):
            return a
        arr=self.get()
        # print(arr,ind,self.val)
        for item in arr:
                i=0
                if(self.val!=""):
                    i=1
                j=len(item[0])-1
                while(i<j):
                    if(item[0][i]!=item[0][j]):
                        break
                    i+=1
                    j-=1
                if(i>=j and item[1]!=ind):
                    a.append([item[1],ind])
                
        return a
    def get(self):
        ans=[]
        for item in self.child:
            if(item):
                ans.extend(item.get())
        for i in range(len(ans)):
            ans[i][0]=self.val+ans[i][0]
        if(self.isEnd):
            ans.append([self.val,self.index])
        return ans