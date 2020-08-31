#1
favemusic = ["Taylor Swift", "bon iver", "jawbreaker", "blink 182"]

#2
places = []
gibsons = (49.3974, 123.5152)
vancouver = (49.2827, 123.1207)
tokyo = (35.6762, 139.6503)
places.append(gibsons), places.append(vancouver), places.append(tokyo)

#3
my_dict = {"height":"6 Feet", "eye color":"blue", "hair color":"blond", "fiance's name":"Lisa","cat names":"fred and george"}

#4
def askme() :
    attr = ""
    list1 = []
    for i in my_dict :
            list1.append(i)
    for j in range(len(list1)-1) :
        attr += list1[j] + ", "
    attr += "or " + list1[-1]

    x = input("Which of these things would you like to know about me: " + attr + "? (type exit to quit)" + "\n")
    if x.lower() in my_dict :
        var = x.lower()
        print(my_dict[var])

    elif (x.lower() == "exit") :
        print("Thanks, have a nice day!")

    else :
        print("please try again")
        askme()
askme()

#5
bandsongs = {"bon iver":"315 creeks", "taylor swift":"lover", "blink 182":"man overboard"}

#6
#Sets are great because they don't allow duplicate values, also good for unions and intersections

