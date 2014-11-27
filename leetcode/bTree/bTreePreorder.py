
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        list = []
        self.iterative_preorder(root,list)

    def iterative_preorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                list.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return list

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
    def insertLeft(self,value):
        self.left=TreeNode(value)
        return self.left

    def insertRight(self,value):
        self.right=TreeNode(value)
        return self.right

if __name__ == '__main__':
    tree=TreeNode("1")
    left = tree.insertLeft("2")
    right = tree.insertRight("3")
    right.insertLeft("4")
    right.insertRight("5")
    so = Solution()
    print so.preorderTraversal(tree)
