Input = "Hello world, today is Monday and it is sunny!"

import numpy as np
from numpy.random import choice
from collections import Counter


class MCModel(object):

    def __init__(self):
        self.transition_matrix = None

    def fit(self, data):
        data_pairs = [data[i:i+2] for i in xrange(len(data)-1)]

        char2next = {}
        for d in data_pairs:
            if d[0] in char2next:
                char2next[d[0]] += d[1]
            else:
                char2next[d[0]] = [d[1]]

        char2index = {c: i for c in enumerate(char2next.keys())}
        index2char = {i: c for c in enumerate(char2next.keys())}
        transition_matrix = np.zeros((len(char2index), len(char2index)))
        for c, v in char2next.iteritems():
            counter = Counter(v)
            for cnext, ccount in counter.iteritems():
                transition_matrix[char2index[c], char2index[cnext]] = ccount
        transition_matrix /= np.sum(transition_matrix, axis=0)

        self.transition_matrix = transition_matrix
        self.char2index = char2index
        self.index2char = index2char
        self.training_data = data

    def predict(self, first_char=None, num_char=10):
        if self.transition_matrix is None:
            raise ValueError('Fit the model first')
        if not first_char:
            first_char = choice(list(self.char2index.keys()))
        if first_char not in self.char2index.keys():
            raise ValueError('First character not in the training data')
        prediction = first_char
        indices = np.arange(self.transition_matrix.shape[0])

        for i in xrange(num_char - 1):
            current_char = prediction[i]
            next_char_index = choice(
                indices, self.transition_matrix[self.char2index[current_char], :])
            next_char = self.index2char[next_char_index]
            prediction += next_char

        return prediction
