# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next: return head
        fast = slow = head
        while fast:
            if fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                slow = slow.next
                break
        tmpHead = slow
        dummy = ListNode(0)
        while tmpHead:
            tmp = dummy.next
            dummy.next = tmpHead
            tmpHead = tmpHead.next
            dummy.next.next = tmp

        head2 = dummy.next
        dummy = ListNode(0)
        p = dummy
        while head:
            p.next = head
            head = head.next
            if head2:
                p.next.next = head2
                head2 = head2.next
            else:
                p.next.next = None
                break
            p = p.next.next


        return dummy.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    so = Solution()
    head = so.reorderList(node1)
    while head:
        print head.val
        head = head.next