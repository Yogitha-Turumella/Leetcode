class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        sum_ = 0
        pro = 1
        while n>0:
            d = n%10
            digits.append(d)
            sum_ +=d
            pro*=d
            n//=10
        return pro-sum_