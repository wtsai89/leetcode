class ListNode:
    def __init__(self, x = 0, n = None):
        self.val = x
        self.next = n


def createLL(arr):
    head = ListNode(arr[0])
    curr = head
    for i in arr[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    
    return head

def listify(head):
    a = []
    while(head):
        a.append(head.val)
        head = head.next
    
    return a
