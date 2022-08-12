class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length=len(words[0])
        d={}
        for item in words:
            if(item in d):
                d[item]+=1
            else:
                d[item]=1
        i=0
        ans=[]
        # print(d)
        while(i<=(len(s)-(len(words)*word_length))):
            d1={}
            c=0
            for j in range(i,len(s),word_length):
                word=s[j:j+word_length]
                # print(word,i,j)
                if((d1.get(word,0)+1)<=d.get(word,0)):
                    if(word not in d1):
                        d1[word]=1
                    else:
                        d1[word]+=1
                    c+=1
                else:
                    break
            if(c==len(words)):
                ans.append(i)
            i+=1
        return ans
        
            
            
            