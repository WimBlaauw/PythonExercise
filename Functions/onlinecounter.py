

def online_count(statuses):
    onlinecount1 = 0 

    for value in statuses.values(): 
        if value == "online":
            onlinecount1 += 1
    if onlinecount1 == 0:
        print("There are no users online.")
    elif onlinecount1 == 1:
        print("There is 1 user online")
    else:
        print("There are " + str(onlinecount1) + " users online.") 
online_count({'Alice': 'offline', 'Bob': 'online'})