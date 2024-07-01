# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_=0
        n1=0
        n2=0
        power=0
        while l1 is not None:
            n1+=l1.val*(10**power)
            power+=1
            l1=l1.next
        power=0
        while l2 is not None:
            n2+=l2.val*(10**power)
            power+=1
            l2=l2.next
        
        sum_=n1+n2
        print(n1,n2,sum_)
        
        list_sum=[int(x) for x in str(sum_)][::-1]
        new_head=ListNode(list_sum[0])
        new_head.next=None
        return_head=new_head
        i=1
        while i<len(list_sum):
            print(i,list_sum[i])
            new_head.next=ListNode(list_sum[i],None)
            new_head=new_head.next
            i+=1
        return return_head
        