# 長度為偶數 的 字符數

class Solution:
    def findNumbers(self, nums) -> int:
        count=0;
        for item in nums:
            if len(str(item))%2 == 0:
                count += 1
        return count
    
    def findNumbersOfFilter(self,nums) -> int:
       newList = filter(lambda v :  len(str(v))%2 == 0 ,nums)
       print(str(newList))
       return len(list(newList))



if __name__ == '__main__':
    solution = Solution()
    # print(solution.findNumbers([1,2,4,44]))
    print(solution.findNumbersOfFilter([1,2,4,44]))
