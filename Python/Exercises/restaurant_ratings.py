def sum_digit(value, number):
    '''
    Return the number of lists of number 0-9 digits that sums to value.
    '''
    # Impossible combination
    if value > 9 * number or value < 0:
        return 0
    if value == 0:
        return 1
    if number == 1:
        return 1
    lists_number = 0
    # i is the first digit in the list being built
    for i in xrange(min(value + 1, 10)):
        result = sum_digit(value - i, number - 1)
        print('Intermediate sum for value: {}, number: {} is: {}'.format(value - i, number - 1, result))
        lists_number += result
    return lists_number


def number_ratings(ratings):
    n = len(ratings)
    s = sum(ratings)

    if n == 1:
        return s + 1
    # Counting the given set already
    number_ratings = 1
    # Case of sums below
    for k in xrange(s):
        number_ratings += sum_digit(k, n)

    print('Before tie cases, number is {}'.format(number_ratings))
    # Tie cases
    # number of digits at the beginning conserved
    next_sum = s
    for k in xrange(n - 1):
        init = ratings[k]
        # changing the current digit to j
        for j in xrange(init):
            number_ratings += sum_digit(next_sum - j, n - k - 1)
        next_sum = next_sum - init
        print('Tie case number {}, number is {}'.format(k, number_ratings))

    return number_ratings
