'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0


def count_th(word):
    global count
    if len(word) < 2:
        return count
    if word[0] + word[1] == "th":
        count = count + 1
        newWord = word[1:]
        count_th(newWord)
    if word[0] + word[1] != "th":
        newWord = word[1:]
        count_th(newWord)
    return count
