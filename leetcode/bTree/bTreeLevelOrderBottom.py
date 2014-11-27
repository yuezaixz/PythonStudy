# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root : return []
        resutList = []
        self.getResult([root],resutList)
        return resutList[::-1]

    def getResult(self,nodeList,resutList):
        result = []
        levelNodeList = []
        for node in nodeList:
            result.append(node.val)
            if node.left : levelNodeList.append(node.left)
            if node.right : levelNodeList.append(node.right)

        resutList.append(result)
        if levelNodeList : self.getResult(levelNodeList, resutList)
            

if __name__ == '__main__':
    tree=TreeNode("1")
    so = Solution()
    print so.levelOrderBottom(tree)
