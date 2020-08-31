#Challenges
# 1
tv = ["The Walking dead", "entourage", "the sopranos", "the vampire diaries"]
for shows in tv :
    print(shows)

# 2
for num in range(25,51) :
    print(num)

# 3
for shownum in tv :
    print(tv.index(shownum))
    print(shownum)

# 4
numlist = [3,6,34,6,5,7,8,4,14,67,342,666,420,69,69420]

while True :
    answer = input("Guess a number on the list: " + "(enter q to quit)\n")
    if (answer == "q") :
        print("Have a nice day!")
        break
    elif (int(answer) in numlist) :
        print("correct! " + answer + " is in the list!")
        print("have a nuce day!")
        break

# 5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []
for i in list1 :
    for j in list2 :
        list3.append(i * j)
print(list3)



