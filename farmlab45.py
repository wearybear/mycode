#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# part1 write a loop that returns all the animals from the NE Farm!
NE_animals= farms[0]["agriculture"]

for x in NE_animals:
     print(x)

# part2 Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.
for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
        print("Plants/Animals raised on", farm["name"])
        for item in farm["agriculture"]:
            print("-", item)

# part3 Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.
yuck= ["carrots", "celery"]

for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
        for ag_item in farm["agriculture"]:
            if ag_item not in yuck:
                 print(ag_item)



# JM
