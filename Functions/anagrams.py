from logging.config import listen

def is_anagram(string1, string2):

    sort1 = sorted(string1)
    sort2 = sorted(string2)

    if sort1 == sort2:
        anagram = True
        return (anagram)
    else:
        anagram = False
        return (anagram)
