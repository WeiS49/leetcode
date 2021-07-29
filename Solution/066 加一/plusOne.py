
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        length = len(digits)
        for i in range(length):
            num += digits[i] * pow(10, length-i-1)
        return [int(i) for i in str(num+1)]







        