class Solution:
    def iterative_postorder(self, root, list):
        stack = []
        pre = None
        if root:
            stack.append(root)
            while stack:
                curr = stack[len(stack) - 1]
                if (curr.left == None and curr.right == None) or (pre and (pre == curr.left or pre == curr.right)):
                    list.append(curr.val)
                    stack.pop()
                    pre = curr
                else:
                    if curr.right: stack.append(curr.right)
                    if curr.left: stack.append(curr.left)
        return list
    
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        list = []
        self.iterative_postorder(root,list)
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
    for val in so.postorderTraversal(tree):
        print val