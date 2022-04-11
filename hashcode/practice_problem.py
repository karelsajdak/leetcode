with open ("e_elaborate.in.txt", "r") as myfile: data = myfile.read().splitlines()
amountCustomers = data[0]

allLikes = []
allDislikes = []
for index in range(1, int(amountCustomers) * 2, 2):
    ingredients = data[index].split(" ")
    for like in range(1, len(ingredients)):
        if ingredients[like] not in allDislikes and ingredients[like] not in allLikes:
            allLikes.append(ingredients[like])
    ingredients = data[index + 1].split(" ")
    for dislike in range(1, len(ingredients)):
        if ingredients[dislike] not in allDislikes:
            if ingredients[dislike] in allLikes:
                allLikes.remove(ingredients[dislike])
            allDislikes.append(ingredients[dislike])
pizza = str(len(allLikes))
for val in allLikes:
    pizza += " " + val
f = open("e.txt", "w")
f.write(pizza)
print(pizza)