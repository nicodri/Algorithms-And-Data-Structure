class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        string = 'Data: {} \n'.format(self.data)
        next_string = 'None' if self.next is None else 'Yes'
        string += 'Next: {}'.format(next_string)

        return string

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    """LinkedList is define by its head Node only"""
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        string = str(self.head.data)
        current = self.head.next

        while current is not None:
            string += ' --> {}'.format(current.data)
            current = current.next

        return string

    def appendToTail(self, data):
        end = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = end

    def deleteNode(self, data):
        current = self.head

        while current.next is not None:
            if current.data == data:
                current.data = current.next.data
                current.next = current.next.next
            current = current.next

    def loopDetection(self):
        ''' Detect if the LinkedList contains a loop'''
        if self.head.next is None:
            print 'No loop'
            return False
        # Intializing two pointers with the runner technique
        slow = self.head
        fast = self.head.next
        while slow != fast:
            if slow.next is None or slow.next.next is None:
                print 'No loop'
                return False
            slow = slow.next
            fast = fast.next.next
        # Loop has been detected
        # Pointers are at the same place, shift slow to the beginning
        slow = self.head
        fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        print 'Loop detected with looping node :', slow
        return True

        
