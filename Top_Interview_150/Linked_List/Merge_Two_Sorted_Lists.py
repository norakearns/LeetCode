class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

        Return the head of the merged linked list.

        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        """
        dummy = ListNode(0) # -> [0,1,1,2,...]
        cur = dummy
        while list1 and list2:
            l1_val = list1.val
            l2_val = list2.val
            if l1_val < l2_val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next
    
        if list1:
            cur.next = list1

        if list2:
            cur.next = list2

        return dummy.next # dummy.next is the real head