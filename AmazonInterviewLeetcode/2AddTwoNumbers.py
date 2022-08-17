# Definition for singly-linked list.
#https://leetcode.com/problems/add-two-numbers/submissions/
#https://www.youtube.com/watch?v=wgFPrzTjm7s&ab_channel=NeetCode
#O(n)
#O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        tail = head
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            total = total % 10
            tail.next = ListNode(total)

            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


list1 = [2,4,3]
list2 = [5,6,4]
sol = Solution()

head1 = ListNode()
l1 = head1
for i in list1:
    l1.next = ListNode(i)
    l1 = l1.next

head2 = ListNode()
l2 = head2
for i in list2:
    l2.next = ListNode(i)
    l2 = l2.next
list = sol.addTwoNumbers(head1.next, head2.next)
