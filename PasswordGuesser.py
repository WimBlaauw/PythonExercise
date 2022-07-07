from traceback import print_list

password = "hello"
passwordprompt = input("Enter password:")
while passwordprompt != password:
    passwordprompt = input("Enter password:")
    if passwordprompt == password:
        break
