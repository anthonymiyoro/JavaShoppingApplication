# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    print (l1)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print (l2)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print (result.val),
        result = result.next

mySolution = Solution()
mySolution.addTwoNumbers([2,4,3], [5,6,4], c = 0)
