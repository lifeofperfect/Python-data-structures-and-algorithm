class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_tail(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        ltr = self.head
        while ltr.next:
            ltr = ltr.next

        ltr.next = Node(data, None)

    def insert_list(self, dataList):
        self.head = None
        for data in dataList:
            self.insert_tail(data)

    def print(self):
        if self.head is None:
            print("Head is empty")

        ltr = self.head
        ltrstr = ""
        while ltr:
            ltrstr += str(ltr.data) + "-->"
            ltr = ltr.next
        print(ltrstr)

    def get_count(self):
        ltr = self.head
        count = 0
        while ltr:
            ltr = ltr.next
            count += 1
        return count

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_count():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_head(data)
            return

        ltr = self.head
        count = 0
        while ltr:
            if count == index - 1:
                ltr.next = Node(data, ltr.next)
                return
            ltr = ltr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_count():
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next

        ltr = self.head
        count = 0
        while ltr:
            if count == index - 1:
                ltr.next = ltr.next.next
                break
            ltr = ltr.next
            count += 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_head(10)
    ll.insert_head(20)
    ll.insert_tail(30)
    ll.print()
    print("it countains", ll.get_count())
    ll.insert_list(["dog", "chicken", "rat", "pig"])
    ll.print()
    print("it countains", ll.get_count())
    ll.insert_at(2, "perfect")
    ll.print()
    ll.remove_at(2)
    ll.print()
