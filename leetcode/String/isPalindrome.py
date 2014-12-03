class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s : return True
        s = filter((lambda x:x.isalnum()),s).lower()
        return s == s[::-1]

if __name__ == '__main__':
    so = Solution()
    print so.isPalindrome("")
    print so.isPalindrome("A man, a plan, a canal: Panama")
    print so.isPalindrome("race a cdar")
    print so.isPalindrome("1a2")