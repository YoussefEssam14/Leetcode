class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            digits = list(map(int,str(n)))
            if len(digits) < 3:  
                return 0
            counter = 0
            for i in range(1,len(digits) - 1):
                if digits[i] > digits[i-1] and digits[i] > digits[i+1]:
                    counter += 1
                elif digits[i] < digits[i-1] and digits[i] < digits[i+1]:
                    counter +=1
            return counter
        return sum(waviness(n) for n in range(num1,num2+1))
                    
            
