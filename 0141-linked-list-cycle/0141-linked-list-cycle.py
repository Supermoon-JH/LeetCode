# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        try:
            while head:
                if id(head) in visited:
                    raise RuntimeError("Found cycle in the ListNode")
                visited.add(id(head))
                head = head.next
        except RuntimeError:
            return True