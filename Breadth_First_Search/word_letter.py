import queue
from string import ascii_lowercase

def word_letter(begin_word, end_word, words=[]):
    word_set = set()
    for word in words:
        word_set.add(word)
    print(word_set)
    if end_word not in word_set:
        return 0

    word_queue = queue.Queue()
    word_queue.put(begin_word)
    print(word_queue)

    level = 1
    while not word_queue.empty():
        n = word_queue.qsize()
        # print(n)
        for i in range(n):
            current_word = word_queue.get()
            # print(current_word)
            current_char = list(current_word)
            # print(current_char)
            for j in range(len(current_char)):
                original_char = current_char[j]
                # print(original_char)
                for c in ascii_lowercase:
                    # print(c)
                    if current_char[j] == c:
                        continue
                    current_char[j] = c
                    final_word = ' '.join(current_char)
                    # print(final_word)
                    if final_word == end_word:
                        level += 1
                        print(level)
                    if final_word in word_set:
                        word_queue.append(final_word)
                        word_set.remove(final_word)

                current_char[j] = original_char

        level += 1

    return 0

if __name__ == '__main__':
    begin_word = 'hit'
    end_word = 'cog'

    word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

    levels = word_letter(begin_word, end_word, word_list)
    print(levels)