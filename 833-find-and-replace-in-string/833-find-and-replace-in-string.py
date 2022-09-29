class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        arr=[[indices[i],sources[i],targets[i]] for i in range(len(indices))]
        arr.sort()
        ans=[]
        curr=0
        for i in range(len(arr)):
            ind,sou,tar=arr[i]
            if(curr<ind):
                for j in range(curr,ind):
                    ans.append(s[j])
                curr=ind
            j=ind
            while(j<len(s) and j<ind+len(sou)):
                if(s[j]!=sou[j-ind]):
                    break
                j+=1
            if(j==ind+len(sou)):
                for item in tar:
                    ans.append(item)
                curr=ind+len(sou)
            # print(curr)
        while(curr<len(s)):
            ans.append(s[curr])
            curr+=1
        return "".join(ans)
        