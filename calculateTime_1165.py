class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        temp = 0
        count = 0
        for ele in word:
            count += abs(temp-keyboard.index(ele))
            
            temp = keyboard.index(ele)
            
        return count