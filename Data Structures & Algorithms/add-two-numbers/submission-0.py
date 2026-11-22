# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #dummy node so i dont have to deal with edge cases
        dummy = ListNode()
        curr = dummy 

        #remember carry value (2nd edge case) set it to 0
        carry = 0

        #iterating until each one has a digit
        while l1 or l2 or carry:

            #we know one of them could be null so we get digits from them, v1 is gonna be the digits of l1
            #only if l1 is not null, if l1 is null set to 0
            v1 = l1.val if  l1 else 0
            #same thing for v2
            v2 = l2.val if l2 else 0

            #now adding up
            val = v1+v2 + carry

            #for 2nd edge case, for 2 digit answers
            carry = val//10

            #
            val = val%10

            curr.next = ListNode(val)

            #update pointer
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        #8+7

        return dummy.next









        