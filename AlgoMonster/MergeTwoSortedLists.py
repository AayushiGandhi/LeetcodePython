# Definition for singly-linked list.
# Time Complexity: O(n+m)
#   n = no of nodes in list1
#   m = no of nodes in list2
# - Memory Complexity: O(1)
# - We have a constant space, since we are just shifting the pointers

#https://www.youtube.com/watch?v=XIdigk956u0&ab_channel=NeetCode
#https://leetcode.com/problems/merge-two-sorted-lists/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        print(head.next.val)
        return head.next

list1 = [1,2,4]
list2 = [1,3,4]
sol = Solution()

l1 = ListNode()
for i in list1:
    l1.next = ListNode(i)
    l1 = l1.next

l2 = ListNode()
for i in list2:
    l2.next = ListNode(i)
    l2 = l2.next
list = sol.mergeTwoLists(l1, l2)
