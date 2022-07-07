def mid(word):
    if len(word)%2 == 0:
        pos = int(len(word)/2)
        return(word[pos])
    else:
        return ""
