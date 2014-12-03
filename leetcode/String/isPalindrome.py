class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s : return True
        s = filter(isAlpha,s).lower()
        return s == s[::-1]

def isAlpha(s):
    return s.isalpha() or s.isdigit()


if __name__ == '__main__':
    so = Solution()
    print so.isPalindrome("")
    print so.isPalindrome("A man, a plan, a canal: Panama")
    print so.isPalindrome("race a car")
    print so.isPalindrome("1a2")