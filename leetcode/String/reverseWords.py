class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # default split by space and trim multi space
        return " ".join(s.split()[::-1])

    def old_reverseWords(self, s):
        stack = []
        word = []
        for temp in s:
            if temp.isspace():
                if word:
                    stack.append("".join(word))
                    word = []
            else:
                word.append(temp)
        if word:
            stack.append("".join(word))
            word = []
        while stack:
            word.append(stack.pop())
        return " ".join(word)

if __name__ == '__main__':
    so = Solution()
    print so.reverseWords("   a   b ")