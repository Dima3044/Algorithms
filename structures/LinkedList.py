class ListNode():
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def add(self, val):
        new_node = ListNode(val, self.next)
        self.next = new_node

    def append(self, value):
        next_el = self
        while next_el.next is not None:
            next_el = next_el.next
        next_el.add(value)

    def __str__(self):
        tmp = self
        s = ''
        while tmp is not None:
            s += str(tmp.value) + ' '
            tmp = tmp.next
        return s

    def list_to_linked_list(self, arr):
        self.value = arr[0]
        for i in range(1, len(arr)):
            self.append(arr[i])


green = ListNode()
arr = [1, 2, 3, 4, 5]

green.list_to_linked_list(arr)

print(green)