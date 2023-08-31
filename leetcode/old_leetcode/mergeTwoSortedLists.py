import logging
logging.basicConfig(level=logging.DEBUG)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.mergeTwoLists(ListNode([1,2,4]), ListNode([1,3,4]))
    
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head=merged_list=ListNode(0)

        logging.debug(list1.val)
        logging.debug(list1.next)

        while(list1 and list2):
            logging.debug(list1.val)
            if list1.val<list2.val:
                merged_list.next=list1
                list1=list1.next
            else:
                merged_list.next=list2
                list2=list2.next
            merged_list=merged_list.next

        merged_list.next= list1 or list2

        logging.debug(head.val)
        logging.debug(merged_list.val)
        logging.debug(head.next)
        return head.next




instance=Solution() 