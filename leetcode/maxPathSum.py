# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if not root: return None
        return self.getPathSum(root )[0]
    def getPathSum(self,root):
        leftSum = rightSum = maxSum = None
        if root.left:
            leftPathResult = self.getPathSum(root.left)
            leftSum = max(leftPathResult[1],leftPathResult[2])
            maxSum = max(maxSum,leftPathResult[0])
        if root.right:
            rightPathResult = self.getPathSum(root.right)
            rightSum = max(rightPathResult[1],rightPathResult[2])
            maxSum = max(maxSum,rightPathResult[0])
        if not leftSum or leftSum < 0 :leftSum = 0
        if not rightSum or rightSum < 0 :rightSum = 0
        maxSum = max(maxSum , root.val + leftSum + rightSum)

        return maxSum,leftSum+root.val,rightSum+root.val

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    leftR = TreeNode(4)
    leftL = TreeNode(5)
    rightR = TreeNode(6)
    rightL = TreeNode(7)
    left.left = leftL
    left.right = leftR
    right.left = rightL
    right.right = rightR
    root.left = left
    root.right = right


    so = Solution()
    print so.maxPathSum(root)