# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def helper(l1, l2):

            head = ListNode(0)
            cur = head

            while l1 and l2:

                if l1.val >= l2.val:
                    cur.next = l2
                    l2 = l2.next
                
                else:
                    cur.next = l1
                    l1 = l1.next
                
                cur = cur.next
            
            if l1:
                cur.next = l1
            
            if l2:
                cur.next = l2

            return head.next

        
        while len(lists) > 1:

            l1, l2 = lists.pop(), lists.pop()
            newList = helper(l1, l2)

            lists.append(newList)
        
        return lists[0] if lists else None