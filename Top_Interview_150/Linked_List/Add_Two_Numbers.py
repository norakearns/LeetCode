class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        """
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            sum = l1_val + l2_val + carry
            if sum > 9:
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            node = ListNode(sum) # Create a list node object
            cur.next = node # [0, 7]
            cur = cur.next # cur is now at node where value is 7

        if carry:
            node = ListNode(1) 
            cur.next = node

        return dummy.next
