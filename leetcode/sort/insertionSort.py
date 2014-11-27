# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            # sort by asc , so , do insertion when current more than current's next 
            if curr.next.val < curr.val:
                # start search the position from dummy
                pre = dummy
                # find the position's pre
                while pre.next.val < curr.next.val:
                    pre = pre.next
                # remove current's next
                temp = curr.next
                curr.next = temp.next
                # and move it to pre's next
                temp.next = pre.next
                pre.next = temp
            else:
                curr = curr.next
        return dummy.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node1.next = node2
    so = Solution()
    head = so.insertionSortList(node1)
    while head:
        print head.val
        head = head.next