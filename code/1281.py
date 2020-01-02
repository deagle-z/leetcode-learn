# 整数的各位积和之差
from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        tem ,sum=1, 0
        for i in str(n):
            tem*=int(i)
            sum+=int(i)
        return tem-sum

    def subtractProductAndSumOfListGenearte(self,n:int)->int:
        # 使用列表生成式
        nums = [int(i) for i in str(n)]
        return reduce(lambda x,y:x*y,nums) - reduce(lambda x,y: x+y,nums)