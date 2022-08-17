# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeSortList(l1, l2))
            lists = mergedLists

        return lists[0]

    def mergeSortList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

l = []
list1 = [1,4,5]
list2 = [1,3,4]
list3 = [2,6]
sol = Solution()

l1_head = ListNode()
l1 = l1_head
for i in list1:
    l1.next = ListNode(i)
    l1 = l1.next

l2_head = ListNode()
l2 = l2_head
for i in list2:
    l2.next = ListNode(i)
    l2 = l2.next

l3_head = ListNode()
l3 = l3_head
for i in list3:
    l3.next = ListNode(i)
    l3 = l3.next

l.append(l1_head.next)
l.append(l2_head.next)
l.append(l3_head.next)

list = sol.mergeKLists(l)