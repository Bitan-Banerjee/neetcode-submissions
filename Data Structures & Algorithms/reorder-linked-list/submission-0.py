# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head == None: return 

        # Lets put all the nodes into a stack
        # Intention is to pop from last and insert in middle
        stack = deque()
        current = head
        while current != None:
            stack.append(current)
            current = current.next
        
        # print(stack)

        # insert nodes from last to middle
        current = head
        while True:
            if current == stack[-1] or current.next == stack[-1]:
                break
            temp = current.next
            current.next = stack[-1]
            stack.pop()
            stack[-1].next = None
            current = current.next
            current.next = temp 
            current = current.next

        return