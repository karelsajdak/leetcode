import time
start_time = time.time()
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        resultListNode = ListNode()
        lastNode = resultListNode
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    lastNode.next = list1
                    list1 = list1.next
                else:
                    lastNode.next = list2
                    list2 = list2.next
            else:
                if list1:
                    lastNode.next = list1
                    list1 = list1.next
                else:
                    lastNode.next = list2
                    list2 = list2.next
            lastNode = lastNode.next
        return resultListNode.next

list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
solution = Solution()
print(solution.mergeTwoLists(list1, list2))
print("--- %s seconds ---" % (time.time() - start_time))