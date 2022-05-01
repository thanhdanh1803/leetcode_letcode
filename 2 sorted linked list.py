# # Definition for singly-linked list.
#debug for understanding linked list in python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# dummy = ListNode()
# print(dummy.val, dummy.next)
# tail = dummy
# print(dummy.__repr__(), tail.__repr__())
# print(tail.val, tail.next)

# a = ListNode(1)
# b = ListNode(3)
# list1 = ListNode(a, b)
# print('list1',list1.val, list1.next)
# tail.next = list1
# print('c',dummy.__repr__(), tail.__repr__())
# print('tail1', tail.val, tail.next)
# print('d',dummy.val, dummy.next)
# tail = tail.next
# print('tail2', tail.val, tail.next)
# print(dummy.val, dummy.next)
# print(dummy.__repr__(), tail.__repr__())
# print(dummy.next.val.val)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while True:
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        return dummy.next
            