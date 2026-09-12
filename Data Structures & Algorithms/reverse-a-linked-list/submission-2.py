# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # YT SHORT : https://youtube.com/shorts/1hw4LHpmc68?si=ErSLwKLrdzoCWxzf
        prev = None
        curr = head
        #NextNode = None

        while curr:
            NextNode = curr.next
            curr.next = prev
            prev = curr
            curr = NextNode
        return prev # now, the prev is the head

        
        