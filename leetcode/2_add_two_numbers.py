# 2. Add Two Numbers
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a
# single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        unit = ((l1.val or 0) + (l2.val or 0)) % 10
        carry = ((l1.val or 0) + (l2.val or 0)) / 10
        l_result = l_sum = ListNode(unit)
        l1 = l1.next
        l2 = l2.next
        while (l1 or l2):
            if l1 and l2:
                unit = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) / 10
                l_sum.next = ListNode(unit)
                l_sum = l_sum.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                unit = (l1.val + carry) % 10
                carry = (l1.val + carry) / 10
                l_sum.next = ListNode(unit)
                l_sum = l_sum.next
                l1 = l1.next
            else:
                unit = (l2.val + carry) % 10
                carry = (l2.val + carry) / 10
                l_sum.next = ListNode(unit)
                l_sum = l_sum.next
                l2 = l2.next
        if carry:
            l_sum.next = ListNode(carry)
        return l_result


# 1559 / 1559 test cases passed.
# Status: Accepted
# Runtime: 149 ms
