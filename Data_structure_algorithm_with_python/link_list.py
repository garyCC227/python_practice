'''
link list vs array
1)search: 差不多啦
2)remove: why we love link list
3) array is memory friendly, since link list need memory for reference
    or pointer

            link list                 array
search          O(n)         O(1) if we know the index

inseart
at start        O(1)            O(n)!!!

inseart
at end          O(N)            O

memoery
waste           O(N)            0
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self, size=0):
        self.head = None
        self._size = 0

    #insert at the head as always
    def insert_head(self, data):
        newNode = Node(data)
        self._size += 1

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    @property
    def size(self):
        return self._size

    def insert_end(self, data):
        newNode = Node(data)
        self._size += 1

        curr = self.head
        while curr.nextNode is not None:
            curr = curr.nextNode

        curr.nextNode = newNode

    def remove(self, data):
        if not self.head:
            return

        prev = None
        curr = self.head
        while curr:
            if curr.data == data:
                if prev == None:
                    self.head = curr.nextNode
                else:
                    prev.nextNode = curr.nextNode
                self._size -= 1
                break

            prev = curr
            curr = curr.nextNode


    def show(self):
        curr = self.head
        while curr:
            print("{0}, ".format(curr.data), end="")
            curr = curr.nextNode
        print('')



if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_head(5)
    linkedlist.insert_head(1)
    linkedlist.insert_head(2)
    linkedlist.insert_head(4)
    linkedlist.insert_end(6)
    linkedlist.show()
    print(linkedlist.size)

    linkedlist.remove(5)
    linkedlist.remove(6)
    print(linkedlist.size)
