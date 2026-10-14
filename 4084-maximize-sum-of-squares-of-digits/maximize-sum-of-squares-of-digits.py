class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num:
            return""
        nine=sum//9
        remainder=sum%9
        zero=num-nine-(1 if remainder >0 else 0)
        result=""
        result+="9"*nine
        if remainder>0:
            result+=str(remainder)
        result+="0"*zero
        return result