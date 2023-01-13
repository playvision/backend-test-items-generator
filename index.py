import sys
import random

colorsFile = "configs/colors.txt"
adjectivesFile = "configs/adjectives.txt"
itemsFile = "configs/items.txt"

colors = open(colorsFile, "r").readlines()
adjectives = open(adjectivesFile, "r").readlines()
items = open(itemsFile, "r").readlines()

needToCreate = int(sys.argv[1])
canCreate = len(colors)*len(adjectives)*len(items)

print("Can create {} unic items ids".format(canCreate))
print("Need to create {} items".format(needToCreate))

if canCreate < int(needToCreate):
    print("Require number of generated items is too large")
    exit()

generated = []

for color in colors:
    for adjective in adjectives:
        for item in items:
            id = (color+"_"+adjective+"_"+item).replace("\n", "")
            generated.append(id)

random.shuffle(generated)

result = generated[:needToCreate]

with open("result.txt", "w") as f:
    for line in result:
        f.write(f"{line}\n")
