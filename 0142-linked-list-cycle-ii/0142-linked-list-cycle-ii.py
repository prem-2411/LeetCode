
# Definition for singly-linked list is provided by LeetCode.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect whether a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Find the node where the cycle begins
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
