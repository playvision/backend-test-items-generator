import sys
import random

colorsFile = "configs/colors.txt"
adjectivesFile = "configs/adjectives.txt"
itemsFile = "configs/items.txt"

colors = open(colorsFile, "r").readlines()
adjectives = open(adjectivesFile, "r").readlines()
items = open(itemsFile, "r").readlines()

needToCreate = sys.argv[1]
canCreate = len(colors)*len(adjectives)*len(items)

print("Can create {} unic items ids".format(canCreate))
print("Need to create {} items".format(needToCreate))

if canCreate < int(needToCreate):
    print("Require number of generated items is too large")
    exit()

result = []

for color in colors:
    for adjective in adjectives:
        for item in items:
            id = (color+"_"+adjective+"_"+item).replace("\n", "")
            result.append(id)

random.shuffle(result)

with open("result.txt", "a") as f:
    f.truncate(0)  # need '0' when using r+
    f.writelines('\n'.join(result))
