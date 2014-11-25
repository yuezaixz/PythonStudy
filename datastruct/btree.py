class BTree:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

    def insertLeft(self,value):
        self.left=BTree(value)
        return self.left

    def insertRight(self,value):
        self.right=BTree(value)
        return self.right

    def show(self):
        print self.data

def preorder(node):
    if node.data:
        node.show()
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

def inorder(node):
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)

def postorder(node):
    if node.data:
        if node.left:
             postorder(node.left)
        if node.right:
            postorder(node.right)
        node.show()
def getDeepth(node):
    if not node : return 0
    leftDeepth = getDeepth(node.left)
    rightDeepth = getDeepth(node.right)
    if leftDeepth > rightDeepth:
        return leftDeepth + 1
    else:
        return rightDeepth + 1


def getWidth(node):
    if not node : return 0
    maxWidth = -1
    layerNodes = [node]
    while layerNodes:
        tempNodes = []
        currWidth = 0
        for currNode in layerNodes:
            if currNode.left: tempNodes.append(currNode.left)
            if currNode.right: tempNodes.append(currNode.right)
            currWidth += 1
        layerNodes = tempNodes
        maxWidth = max(maxWidth,currWidth)
    return maxWidth

            
                
if __name__ == "__main__":
    
    Root=BTree("root")
    A=Root.insertLeft("A")
    C=A.insertLeft("C")
    D=C.insertRight("D")
    F=D.insertLeft("F")
    G=D.insertRight("G")
    B=Root.insertRight("B")
    E=B.insertRight("E")

    print "pre-traversal"
    preorder(Root)

    print "in-traversal"
    inorder(Root)

    print "post-traversal"
    postorder(Root)

    print "tree-deepth"
    print getDeepth(Root)

    print "tree-width"
    print getWidth(Root)

        
