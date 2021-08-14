
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(length-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0       # 重新赋值 时间复杂度低
            else:
                digits[i] += 1
                return digits
        
        if digits[0] == 0:
            digits.insert(0, 1)
        
        return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(length-1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10      # 涉及计算, 速度相对较慢
            if digits[i] != 0:
                return digits
        
        if digits[0] == 0:
            digits.insert(0, 1)
        
        return digits

