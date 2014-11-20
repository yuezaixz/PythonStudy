class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        list = []
        self.iterative_inorder(root,list)
        return list
        
    def iterative_inorder(self, root, list):
        stack = []
        pre = None
        if root:
            stack.append(root)
            while stack:
                curr = stack[-1]
                # if pre node is right , pop the stack 
                if (pre and (pre == curr.right)):
                    stack.pop()
                    pre = curr
                elif (curr.left == None ) or (pre and (pre == curr.left)):
                    list.append(curr.val)
                    # if current node has right , must pop after handle right
                    # because current node's parent juge whether the left is over by "(pre and (pre == curr.left))"
                    # so i must sure the prev is left , not left's right
                    if curr.right: 
                        stack.append(curr.right)
                    else:
                        stack.pop()
                        pre = curr

                elif curr.left: 
                    stack.append(curr.left)

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
    tree=TreeNode("3")
    left = tree.insertLeft("1")
    # right = tree.insertRight("3")
    # right.insertLeft("4")
    left.insertRight("2")
    so = Solution()
    print so.inorderTraversal(tree)