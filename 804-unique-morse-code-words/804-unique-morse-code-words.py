class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d=[chr(i+97) for i in range(26)]
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        order=(dict(zip(d,a)))
        s=set()
        for item in words:
            t=[]
            for val in item:
                t.append(order[val])
            s.add("".join(t))
        return len(s)