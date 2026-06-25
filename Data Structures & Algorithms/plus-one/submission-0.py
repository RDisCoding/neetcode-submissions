class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        digits = digits[::-1]
        for d in range(len(digits)):
            if digits[d] != 9 :
                digits[d] += 1
                return digits[::-1]
            temp = digits[d]
            temp += carry
            digits[d] = temp % 10
            carry = temp // 10
        if carry:
            digits.append(carry)
        return digits[::-1]
            