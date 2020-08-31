# challenges
import csv
# 1
with open("C:\\Users\\phil\\sonnet29.txt","r") as f :
    var = f.read()
    print(var)

# 2
q = input("do you like cheese? ")
with open("answer.txt","w") as x :
    x.write(q)
    print("Thank you")

list1 = [["top gun", "risky business", "minority report"], ["titanic", "the revenant", "inception"], ["training day", "man on fire", "flight"]]

with open("movies.csv", "w", newline='') as csvfile :
    writer = csv.writer(csvfile, delimiter=",")
    for x in list1 :
        writer.writerow(x)


