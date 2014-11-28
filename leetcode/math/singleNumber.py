class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        curr = 0
        for target in A:
            curr ^= target
        return curr

