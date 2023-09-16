# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # i need to read the digits of the linked lists, reverse their order, and then add them together, reverse them, and then return them as a linked list
        list_i_val=[]
        list_j_val=[]
        for i,j in zip(l1, l2):
            list_i_val.append(i)
            list_j_val.append(j)
        list_j_val=list_j_val.reverse()
        list_i_val=list_i_val.reverse()
        i_str=''
        j_str=''
        for i,j in zip(list_i_val, list_j_val):
            i_str+=i
            j_str+=j
        sum=int(j_str)+int(i_str)
        sum=str(sum)
        l3=ListNode()
