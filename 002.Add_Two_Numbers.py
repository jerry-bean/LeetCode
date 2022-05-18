# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = point = ListNode(0)
        remain = 0
        while l1 or l2:
            new_point = ListNode()
            if (l1 == None):
                new_point.val = (l2.val + remain) % 10
                remain = (l2.val + remain) // 10
                l2 = l2.next
            elif (l2 == None):
                new_point.val = (l1.val + remain) % 10 
                remain = (l1.val + remain) // 10
                l1 =  l1.next
            else:
                new_point.val = (l1.val + l2.val + remain) % 10 
                remain = (l1.val + l2.val + remain) // 10
                l1 = l1.next
                l2 = l2.next
            point.next = new_point
            point = point.next
            
        if remain != 0:
            point.next = ListNode(1)
        return head.next