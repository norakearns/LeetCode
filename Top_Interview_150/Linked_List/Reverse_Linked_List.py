class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

        Input: head = [1,2,3,4,5], left = 2, right = 4
        Output: [1,4,3,2,5]
        """
        if left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy 
        for i in range(1, left):
            prev = prev.next 

        cur = prev.next
        for i in range(0, right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next