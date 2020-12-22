#!/usr/bin/python

allergen_poss = {}

allergy_ings = set()

all_recipes = []

#Weed out all ingredients that do not appear every time an allergen is present
with open('input.txt', 'r') as lines:
    for line in lines.readlines():

        #Remove trailing paren and split into ingredients and allergen info
        ingredients, rec_all = line.strip(')\n').split(" (contains ")
      
        ingredients, rec_all = ingredients.split(" "), rec_all.split(", ")
       
        all_recipes = all_recipes + ingredients

        ingredients = set(ingredients)

        for allergen in rec_all:
            
            if (allergen not in allergen_poss):
                
                allergen_poss[allergen] = ingredients

            else:
                allergen_poss[allergen] = ((allergen_poss[allergen] & ingredients))

#Create a single set with all offending ingredients
for ings in (allergen_poss.values()):

    allergy_ings = allergy_ings | ings

#Find all mentions of non-allergen ingredients
all_recipes = filter(lambda a: a not in allergy_ings, all_recipes)

print(len(all_recipes))
