from queue import Queue
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        myarr={}
        for i in range(len(wordList)):
            myarr[wordList[i]]=i
        a,b=myarr.get(beginWord,-1),myarr.get(endWord,-1)
        if(b==-1):
            return []
        if(a==-1):
            a=len(wordList)
            wordList.append(beginWord)
        myarr[beginWord]=a
        # print(myarr)
        d=[[] for __ in range(len(wordList))]
        for i in range(len(wordList)):
            word=list(wordList[i])
            for j in range(len(word)):
                for k in range(26):
                    test=word[j]
                    if(ord(word[j])==k+97):
                        continue
                    else:
                        word[j]=chr(k+97)
                        t=myarr.get("".join(word),-1)
                        # print("".join(word),i,t)
                        if(t!=-1 ):
                            d[i].append(t)
                        word[j]=test
                        
    
        ans=[]
        return self.get(d,a,b,wordList)
    
    def get(self,d,start,end,wordList):
        obj=Queue()
        ans=len(d)+1
        obj.put([start,1])
        visit=[False for _ in range(len(d))]
        while(not obj.empty()):
            top=obj.get()
            if(top[0]==end):
                ans=min(ans,top[1])
            if(visit[top[0]]):
                continue
            visit[top[0]]=True
            for item in d[top[0]]:
                if(not visit[item]):
                    obj.put([item,top[1]+1])
        if(len(d)+1==ans):
            return []
        # print(ans)
        visit=[False for _ in range(len(d))]
        # print(d)
        return self.find(wordList,start,end,d,ans-1,{},visit)
    
    def find(self,words,start,end,d,ans,store,visited):
        # print(start,end,ans)
        if(start==end and ans==0):
            return [[words[end]]]
        elif((ans<=0) or start==end):
            return []
        elif((start,ans) in store):
            return store[(start,ans)]
        else:
            # print(d[start])
            res=[]
            visited[start]=True
            for item in d[start]:
                if(not visited[item]):
                    a=self.find(words,item,end,d,ans-1,store,visited)
                    # print(item,start,a,ans)
                    for item1 in a:
                        res.append([words[start]]+item1)
            # print(res,words[start])
            visited[start]=False
            store[(start,ans)]=res
            return res