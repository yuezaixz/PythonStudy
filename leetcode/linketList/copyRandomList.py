# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head  : return None
        p = head
        while p:
            p_copy = RandomListNode(p.label)
            p_copy.next = p.next
            p.next = p_copy
            p = p.next.next
        p = head
        while p:
            if p.random : p.next.random = p.random.next
            p = p.next.next
        newhead = head.next
        p = head
        pnew = newhead
        while pnew.next:
            p.next = pnew.next
            p = p.next
            pnew.next = p.next
            pnew = pnew.next
        p.next = None
        pnew.next = None
        return newhead
if __name__ == '__main__':
    node1 = RandomListNode(-1)
    node1.random = None
    print Solution().copyRandomList(node1).label