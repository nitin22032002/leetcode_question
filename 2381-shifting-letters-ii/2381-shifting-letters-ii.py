class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        positive=[[0,0] for _ in range(len(s))]
        negative=[[0,0] for _ in range(len(s))]
        for item in shifts:
            if(item[2]==0):
                negative[item[0]][0]+=1
                negative[item[1]][1]+=1
            else:
                positive[item[0]][0]+=1
                positive[item[1]][1]+=1
        value=[ord(s[_])-96 for _ in range(len(s))]
        scoreP=0
        scoreN=0
        for i in range(len(s)):
            scoreP+=positive[i][0]
            scoreN+=negative[i][0]
            value[i]+=((scoreP+(-scoreN))+26)
            value[i]%=26
            if(value[i]==0):
                value[i]=26
            value[i]=chr(value[i]+96)
            scoreP-=positive[i][1]
            scoreN-=negative[i][1]
        return "".join(value)
        
    