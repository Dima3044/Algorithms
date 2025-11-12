class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, val):
        new_node = ListNode(val, self.next)
        self.next = new_node

    def append(self, val):
        next_el = self
        while next_el.next is not None:
            next_el = next_el.next
        next_el.add(val)

    def list_to_linked_list(self, arr):
        self.value = arr[0]
        for i in range(1, len(arr)):
            self.append(arr[i])
        


def mergeTwoLists(list1, list2):
    answer = []
    while list1 is not None or list2 is not None:
        if list1 is None:
            answer.append(list2.val)
            list2 = list2.next
        elif list2 is None:
            answer.append(list1.val)
            list1 = list1.next

        elif list1.val <= list2.val:
            answer.append(list1.val)
            list1 = list1.next

        elif list2.val < list1.val:
            answer.append(list2.val)
            list2 = list2.next
    output = ListNode()
    output.list_to_linked_list(answer)
    return answer
    

l1 = ListNode()
l1.list_to_linked_list([1, 2, 4])
l2 = ListNode()
l2.list_to_linked_list([1, 3, 4])

a = mergeTwoLists(l1, l2)

print(a)