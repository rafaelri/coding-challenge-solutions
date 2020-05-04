from typing import List
from jeff_kitchen import Ingredient, Kitchen
from hamcrest import *

def test_empty_stock():
    recipes = list()
    stock = list()

    boiled_egg = list()
    boiled_egg.append(Ingredient("egg", 1)) 

    recipes.append(boiled_egg)

    kitchen = Kitchen(recipes, stock)
    assert_that(kitchen.able_to_cook(), equal_to(False))

def test_insufficient_stock():
    recipes = list()
    stock = list()
    stock.append(Ingredient("egg", 1))

    boiled_egg = list()
    boiled_egg.append(Ingredient("egg", 2)) 

    recipes.append(boiled_egg)

    kitchen = Kitchen(recipes, stock)
    assert_that(kitchen.able_to_cook(), equal_to(False))    

def test_insufficient_stock_after_first_recipe():
    recipes = list()
    stock = list()
    stock.append(Ingredient("egg", 3))

    boiled_egg = list()
    boiled_egg.append(Ingredient("egg", 2)) 

    recipes.append(boiled_egg)
    recipes.append(boiled_egg)

    kitchen = Kitchen(recipes, stock)
    assert_that(kitchen.able_to_cook(), equal_to(False))    

def test_sufficient_stock_after_first_recipe():
    recipes = list()
    stock = list()
    stock.append(Ingredient("egg", 5))
    stock.append(Ingredient("water", 3))

    boiled_egg = list()
    boiled_egg.append(Ingredient("egg", 2)) 
    boiled_egg.append(Ingredient("water", 1)) 

    recipes.append(boiled_egg)
    recipes.append(boiled_egg)

    kitchen = Kitchen(recipes, stock)
    assert_that(kitchen.able_to_cook(), equal_to(True))    
