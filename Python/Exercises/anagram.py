# Enter your code here. Read input from STDIN. Print output to STDOUT

# ### Functions


def pyramid(top, bottom, dictionary):
    '''
    Compute if a pyramid exists from top to bottom based the words
    in dictionary.
    '''
    # Debug
    # print('pyramid on {}'.format(pyramid))
    # return get_next_double_dfs([top], {bottom}, dictionary)
    distance = len(bottom) - len(top)
    if distance < 0:
        return False
    # Initialisation
    set_top = set()
    set_top.add(top)

    set_bottom = set()
    set_bottom.add(bottom)
    return get_next(set_top, set_bottom, dictionary, distance)


def get_next(current, bottom, dictionary, distance):
    '''
    Compute the below stage of the pyramids for the word in current
    and return True if bottom is touched.
    Build a bidirectionnal breadth-first search and updates at each
    stage the side with the least number of nodes.
    '''
    # Debug
    # print('get next on {} for {}'.format(current, bottom))

    # Define the way to go
    up = len(bottom) > len(current)

    # Last stage case
    if distance == 0:
        if up:
            return bool(bottom.intersection(current))
        else:
            return bool(current.intersection(bottom))

    # Initialisation
    nexts = current
    next_bottom = bottom
    if up:
        nexts = set()
        for word in list(current):
            nexts = nexts.union(get_anagram(word, dictionary))

    else:
        next_bottom = set()
        for word in list(bottom):
            next_bottom = next_bottom.union(get_prev_anagram(word, dictionary))

    if not (bool(nexts) and bool(next_bottom)):
        return False
    else:
        return get_next(nexts, next_bottom, dictionary, distance - 1)


def get_prev_anagram(word, dictionary):
    '''
    Return list of the possible anagrams of the stage up from
    dictionary for word, as a set.
    '''
    l = len(word)
    anagrams = set()
    if l - 1 in dictionary.keys():
        for candidate in list(dictionary[l - 1]):
            i_candidate = 0
            valid = True
            for (i_word, c) in enumerate(word):
                # word present at the beginning of candidate
                if i_word == l - 1:
                    break
                if (i_word - i_candidate) > 1:
                    valid = False
                    break
                elif c != candidate[i_candidate]:
                    continue
                else:
                    i_candidate += 1
            if valid:
                anagrams.add(candidate)
    # Debug
    # print('get prev anagram on {}, answer is {}'.format(word, anagrams))
    return anagrams


def get_anagram(word, dictionary):
    '''
    Return list of the possible anagrams of the stage below from
    dictionary for word as a list
    '''
    l = len(word)
    anagrams = set()
    if l+1 in dictionary.keys():
        for candidate in list(dictionary[l + 1]):
            i_word = 0
            valid = True
            for (i_candidate, c) in enumerate(candidate):
                # word present at the beginning of candidate
                if i_candidate == l:
                    break
                if (i_candidate - i_word) > 1:
                    valid = False
                    break
                elif c != word[i_word]:
                    continue
                else:
                    i_word += 1
            if valid:
                anagrams.add(candidate)
    # Debug
    # print('get anagram on {}, answer is {}'.format(word, anagrams))
    return anagrams


# ### Reading the Input
import time

if __name__ == "__main__":
    # To determine if a case is left
    start_load = time.time()
    data = open('input.txt').readlines()
    N = data[0]
    N = int(N)
    # Format (l, (set(words of length l), visited))
    dictionary = {}

    for i in xrange(0, N):
        word = sorted(data[i+1].replace('\n', ''))
        l = len(word)
        if l not in dictionary.keys():
            dictionary[l] = set()
        dictionary[l].add(''.join(word))

    M = int(data[N+1])

    # Store the asked pyramids with format (case, (top, bottom))
    tries = {}
    for j in xrange(0, M):
        top, bottom = data[N+2+j].split(' ')
        tries[j] = (
            ''.join(sorted(top)), ''.join(sorted(bottom.replace('\n', ''))))

    end_load = time.time() - start_load
    print 'load time is {}'.format(end_load)
    # ### Main
    j = 1
    print('Case {}:'.format(j))
    for i in xrange(0, M):
        print 'yes' if pyramid(tries[i][0], tries[i][1], dictionary) else 'no'
