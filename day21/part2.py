#!/usr/bin/python

import sys

allergen_poss = {}

allergens = {}

#Weed out all ingredients that do not appear every time an allergen is present
with open('input.txt', 'r') as lines:
    for line in lines.readlines():

        #Remove trailing paren and split into ingredients and allergen info
        ingredients, rec_all = line.strip(')\n').split(" (contains ")
      
        ingredients, rec_all = ingredients.split(" "), rec_all.split(", ")
       
        ingredients = set(ingredients)

        for allergen in rec_all:
            
            if (allergen not in allergen_poss):
                
                allergen_poss[allergen] = ingredients

            else:
                allergen_poss[allergen] = ((allergen_poss[allergen] & ingredients))


while(len(allergen_poss) > 0):
    for aller, ings in allergen_poss.items():

        allergen_poss[aller] = ings.difference(set(allergens.values()))

        if (len(allergen_poss[aller]) == 1): #If there is only one possibility for the culprit

            allergens[aller] = allergen_poss[aller].pop()

            del allergen_poss[aller] 

for allergen in sorted(allergens): #Sort alphabetically by allergen
    sys.stdout.write("%s," % allergens[allergen]) 
