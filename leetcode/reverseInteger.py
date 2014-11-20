class Solution:
    # @return an integer
    def reverse(self, x):
        INT_MAX = 2147483647

        isPostive = True
        if x < 0:
            isPostive = False
            x *= -1
        xStr = str(x)
        index = 1
        result = 0
        while index <= len(xStr):
            tempNum = int(xStr[index*-1])
            if INT_MAX/10 >= result :
                result *= 10
            else:
                return 0
            if INT_MAX - tempNum >= result:
                result += tempNum
            else:
                return 0
            index += 1
        return result * (1 if isPostive else -1)



if __name__ == "__main__":
    so = Solution()
    print so.reverse(1534236469)
