from jeff_kitchen import Ingredient, Kitchen

recipes = list()
stock = list()
stock.append(Ingredient("egg", 5))
stock.append(Ingredient("water", 3))

boiled_egg = list()
boiled_egg.append(Ingredient("egg", 2)) 
boiled_egg.append(Ingredient("water", 1)) 

recipes.append(boiled_egg)

kitchen = Kitchen(recipes, stock)
print(kitchen.able_to_cook())    
