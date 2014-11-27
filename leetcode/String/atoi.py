class Solution:
    # @return an integer
    def atoi(self,str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        start = 0
        result = 0
        isPositive = True
        outScope = False

        if str == "":
            return 0

        while start < len(str) and str[start].isspace():
            start += 1
        if start < len(str) and str[start] == "-":
            isPositive = False
        if start < len(str) and (str[start] == "-" or str[start] == "+"):
            start += 1
        # can't slice str by int(str[start:end]),because the num maybe out of scope
        while start < len(str) and str[start].isdigit() :
            tempNum = int(str[start])
            if INT_MAX/10 >= result:
                result *= 10
            else:
                outScope = True
                break

            if (INT_MAX - tempNum) >= result:
                result += tempNum
            else:
                outScope = True
                break
            start += 1
        if outScope:
            if isPositive:
                result = INT_MAX
            else:
                result = INT_MIN
        else:
            result *= 1 if isPositive else -1  
        return result

if __name__ == "__main__":
    so = Solution()
    print so.atoi("213")
    print so.atoi("-213")