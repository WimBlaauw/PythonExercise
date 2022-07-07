from turtle import position
def capitalpos(text):
    capitals = [index for index in range (len(text)) if text[index].isupper()]
        #ALTERNITIVE capitals = [index for index in range (len(text)) if text[index].isupper()]
    print(capitals)

