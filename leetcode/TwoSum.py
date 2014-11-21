class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        return self.twoSumByDict(num, target)

    def twoSumByDict(self, num, target):
        numDict = {}
        for x in xrange(0,len(num)):
            tempNum = num[x]
            if target-tempNum in numDict:
                return (numDict[target-tempNum]+1,x+1)
            else:
                numDict[tempNum] = x 

    def towSumByErgodic(self, num, target):
        numtosort = num[:]; 
        numtosort.sort()
        result = []
        length = len(numtosort)
        index1 = 0;
        index2 = length-1
        while index2 > index1:
            num1 = numtosort[index1]
            num2 = numtosort[index2]
            if num1 + num2 == target:
                for x in xrange(0,length):
                    if num[x] == numtosort[index1]:
                        result.append(x)
                        break
                for x in xrange(length-1,-1,-1):
                    if num[x] == numtosort[index2]:
                        result.append(x)
                        break
                result.sort()
                break
            # the sum is too big , so num2 need to be smaller
            elif num1 + num2 > target:
                index2 -= 1
            # the sum is too small , so num1 need to be bigger
            else:
                index1 += 1

        return (result[0]+1,result[1]+1)

if __name__ == '__main__':
    so = Solution()
    print so.twoSum([3,2,4],6)