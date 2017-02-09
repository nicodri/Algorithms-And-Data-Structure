class UnionFind(object):
    """docstring for UnionFind"""
    def __init__(self, parent=None):
        self.rank = 1
        if parent is None:
            self.parent = self
        else:
            self.parent = parent

    def get_parent(self):
        if self.parent = self:
            return self
        else:
            return get_parent(self.parent)

    def union(self, group1, group2):
        parent1 = get_parent(group1)
        parent2 = get_parent(group2)

        if parent1 != parent2:
            if parent1.rank > parent2.rank:
                parent2.parent = parent1
                parent1.rank += parent2.rank
            else:
                parent1.parent = parent2
                parent2.rank += parent1.rank


        