class Heap(object):
    """Heap implementation with a Python list, first element starting on index
    1. Values should be stricly non negative integer.
    Type defines type of heap: min heap if type == 1 else max heap"""
    def __init__(self, heap=None, type=1):
        if heap is None:
            self.heap = [0]
        else:
            self.heap = heap
        self.type = type

    def __repr__(self):
        array = self.heap
        return str(array)

    def __len__(self):
        # Retrieve 1 as the heap is initialized with 0
        return len(self.heap) - 1

    def swap_key(self, pointer1, pointer2):
        temp = self.heap[pointer1]
        self.heap[pointer1] = self.heap[pointer2]
        self.heap[pointer2] = temp

    def get_parent_index(self, pointer):
        '''Pointer is an index in the heap list'''
        if pointer == 1:
            return None
        return pointer / 2

    def get_parent_value(self, pointer):
        i = self.get_parent_index(pointer)
        if i:
            return self.heap[self.get_parent_index(pointer)]
        return None

    def get_children_index(self, pointer):
        child1_index = 2 * pointer
        child2_index = 2 * pointer + 1
        if len(self.heap) < child1_index:
            return []
        if len(self.heap) < child2_index:
            return [child1_index]
        return [child1_index, child2_index]

    def get_children_value(self, pointer):
        children_value = []
        for c in self.get_children_index(pointer):
            children_value.append(self.heap[c])
        return children_value

    def insert(self, key):
        # Inserting index at the bottom
        self.heap.append(key)

        # Bubbling-up
        pointer = len(self.heap) - 1
        parent_index = self.get_parent_index(pointer)
        while parent_index:
            # min heap
            if (key < self.heap[parent_index] and self.type) or (key > self.heap[parent_index] and not self.type):
                self.swap_key(pointer, parent_index)
                pointer = parent_index
                parent_index = self.get_parent_index(pointer)
            else:
                break

    def extract_extremum(self):
        # Corner case
        if not len(self):
            return None
        # Extracting root
        root = self.heap[1]
        if len(self.heap) == 1:
            self.heap = [0]
            return root

        # Filling root with bottom leaf
        self.heap[1] = self.heap[-1]

        # Bubbling down
        pointer = 1
        key = self.heap[1]
        children_index = self.get_children_index(pointer)
        children_value = self.get_children_value(pointer)
        while children_value:
            finished = True
            for i, v in enumerate(children_value):
                if (key > v and self.type) or (key < v and not self.type):
                    self.swap_key(pointer, children_index[i])
                    pointer = children_index[i]
                    children_index = self.get_children_index(pointer)
                    children_value = self.get_children_value(pointer)
                    finished = False
                    break
            if finished:
                break

        return root


# Function using heap
# TOFIX: buggy
def compute_median(mylist):
    '''
    Compute the median of mylist using two heaps, useful for online stream of
    data.
    '''
    if len(mylist) < 2:
        return None if not len(mylist) else mylist[0]

    # Build the two heap
    maxheap = Heap(type=0)
    minheap = Heap(type=1)

    # Initialization of the heaps
    if mylist[0] > mylist[1]:
        max_elt = mylist[1]
        min_elt = mylist[0]
    else:
        max_elt = mylist[0]
        min_elt = mylist[1]
    maxheap.insert(max_elt)
    minheap.insert(min_elt)

    # Insertion in the heap

    for v in mylist[2:]:
        print 'Proceeding ', v
        print 'maxheap is ', maxheap
        print 'minheap is ', minheap
        if v < max_elt:
            maxheap.insert(v)
            # Rebalance if needed
            if len(maxheap) > len(minheap) + 1:
                minheap.insert(maxheap.extract_extremum())
        elif v > min_elt:
            minheap.insert(v)
            # Rebalance if needed
            if len(minheap) > len(maxheap) + 1:
                maxheap.insert(minheap.extract_extremum())
        else:
            if len(maxheap) < len(minheap):
                maxheap.insert(v)
            else:
                minheap.insert(v)

        max_elt = maxheap.heap[1]
        min_elt = minheap.heap[1]
    print 'maxheap is ', maxheap
    print 'minheap is ', minheap
    # Retrieve mean
    if len(mylist) % 2 == 1:
        # Retrieve extremum of longest heap
        if len(maxheap) > len(minheap):
            return max_elt
        else:
            return min_elt
    else:
        return (min_elt + max_elt)/2.




        