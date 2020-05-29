from typing import List
from functools import reduce

    
class Ingredient():
    def __init__(self, desc: str, qty: float):
        self.desc = desc
        self.qty = qty

def to_dict(d: dict, i: Ingredient):
    d[i.desc]=i.qty
    return d

class Kitchen():
    def __init__(self, recipes: List[List[Ingredient]], stock: List[Ingredient]):
        self.recipes = recipes
        self.stock = dict()
        self.stock = reduce(to_dict, stock, self.stock)

    def use_ingredient(self, i: Ingredient):
        in_stock = self.stock.get(i.desc)
        if not in_stock:
            return False
        if i.qty > in_stock:
            return False
        else:
            self.stock[i.desc] = in_stock - i.qty
            return True

    def able_to_cook(self):
        for recipe in self.recipes:
            for ingredient in recipe:
                if not self.use_ingredient(ingredient):
                    return False
        return True    
