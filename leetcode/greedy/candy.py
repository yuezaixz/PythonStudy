class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings: return 0;
        length = len(ratings)
        candyNums = [1 for i in xrange(length) ]

        for i in xrange(1,length):
            if ratings[i] > ratings[i-1]:candyNums[i] = candyNums[i-1]+1
        for i in xrange(-2,-(length+1),-1):
            if ratings[i] > ratings[i+1] and candyNums[i] <= candyNums[i+1]:
                candyNums[i] = candyNums[i+1]+1

        return sum(candyNums)


if __name__ == '__main__':
    print Solution().candy([1,2,1])