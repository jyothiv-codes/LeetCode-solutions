# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        process=[]
        final_list=[]
        while head is not None:
            val=head.val
            if val==0:
                if len(process)>0:
                    final_list.append(sum(process))
                    process=[]
            else:
                process.append(val) 
            head=head.next
        #print(final_list)
        curr_head=ListNode()
        dummy=curr_head
        
        for i in range(len(final_list)):
            curr_head.next=ListNode(final_list[i])
            #print("within",curr_head.next.val)
            curr_head=curr_head.next
            
           
        return dummy.next






        


        