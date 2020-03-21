# 请你返回将它变成 0 所需要的步数 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1


class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num==0:
            return 0 
        else :
            return self.numberOfStep(num)-1


    def numberOfStep(self, num: int)-> int:
        total = 1
        if num == 0:
            return total
        elif num % 2 == 0:
            total+=self.numberOfStep(num/2)
            return total
        else:
            total+=self.numberOfStep(num-1)
            return total

if __name__ == '__main__':
    s=Solution()
    print(s.numberOfSteps(14))