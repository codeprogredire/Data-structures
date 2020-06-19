'''
Link: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if fast==slow:
                return True
            
        return False
        
        