import string


def palindrome(string1):
    reverse = string1[::-1]

    if string1 == reverse:
        same = True
        return(same)
    else:
        same = False
        return(same)