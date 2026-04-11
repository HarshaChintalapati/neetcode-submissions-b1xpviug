# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next
        currA, currB = headA, headB 
        diff = abs(lenA - lenB)
        if lenA > lenB:
            a=0
            while(a<diff):
                currA=currA.next
                a+=1
        else:
            b=0
            while(b<diff):
                currB=currB.next
                b+=1
        while currA != currB:
            currA = currA.next
            currB = currB.next    
        return currA




        

        

        

            
        