class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans=[]
        i=0
        j=0
        while(i<len(word1) and j<len(word2)):
            # print((i,j),word1[i],word2[j])
            if(word1[i]>word2[j]):
                ans.append(word1[i])
                i+=1
            elif(word2[j]>word1[i]):
                ans.append(word2[j])
                j+=1
            else:
                a=i
                b=j
                while(a<len(word1) and b<len(word2) and word1[a]==word2[b]):
                    a+=1
                    b+=1
                # print(a,b)
                if(b>=len(word2)):
                    while(i!=a and word1[i]==word2[j]):
                        ans.append(word1[i])
                        i+=1
                elif(a>=len(word1)):
                    while(j!=b and word1[i]==word2[j]):
                        ans.append(word2[j])
                        j+=1
                else:
                    if(word1[a]>word2[b]):
                        while(i!=a and word1[i]==word2[j]):
                            ans.append(word1[i])
                            i+=1
                    else:
                        while(j!=b and word1[i]==word2[j]):
                            ans.append(word2[j])
                            j+=1
        while(j<len(word2)):
            ans.append(word2[j])
            j+=1
        while(i<len(word1)):
            ans.append(word1[i])
            i+=1
        # print(list(enumerate(ans)))
        # print(list(enumerate(list("qqqqqqqqqqqqqqqqqeqqqeqeqqeeqqqeeqqeeqqqqqeq"))))
        return "".join(ans)