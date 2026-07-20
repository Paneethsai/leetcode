class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and not carry:
            return None
            
        val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        node = ListNode(val % 10)
        node.next = self.addTwoNumbers(
            l1.next if l1 else None, 
            l2.next if l2 else None, 
            val // 10
        )
        return node