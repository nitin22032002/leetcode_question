class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        bit=0
        for item in sentence:
            j=ord(item)-97
            b=1<<j
            bit|=b
        for i in range(26):
            b=1<<i
            if(bit&b==0):
                return False
        return True