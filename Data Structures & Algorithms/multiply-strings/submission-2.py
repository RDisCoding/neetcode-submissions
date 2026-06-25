class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        stringToNum = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        numToStr = { i: str(i) for i in range(10)}
        
        def help(numString):
            total = 0
            for i in range(len(numString)-1, -1, -1):
                total += stringToNum[numString[i]]*10**(len(numString)-1-i)
            return total

        num1 = help(num1)
        num2 = help(num2)

        ans = num1*num2
        res = []
        while ans:
            res.append(numToStr[ans%10])
            ans //=10
        if not res:
            return "0"

        res = res[::-1]
        return "".join(res)
