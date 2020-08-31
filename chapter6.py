#Challenges
# 1
camus = "Camus"
for i in camus :
    print(i)

# 2
collect = "yesterday i wrote a " + input("response 1: ") + ". I sent it to " + input("response 2: ") + "!"
print(collect)

# 3
str3 = "aldous Huxley was born in 1894"
print(str3.capitalize())

# 4
str4 = "Where now? Who now? When now?"
list4 = str4.split("? ")
print(list4)

# 5
list5 = ["the", "fox", "jumped", "over", "the", "fence", "."]
str5 = " ".join(list5)
str55 = str5.replace(" .", ".")
print(str55)

# 6
str6 = "A screaming comes across the sky"
str66 = str6.replace("s", "$")
print(str66)

# 7
str7 = "Hemingway"
print(str7.index("m"))

# 8
quote = "\"so then, she went upstairs, ate them herself, and then...\""

# 9
str9 = "three"
str99 = str9 + str9 + str9
str999 = ((str9 + " ") * 3).strip()
print(str999)

# 10
ten = "It was a bright cold day in April, and the clocks were striking thirteen"
print(ten[:33])