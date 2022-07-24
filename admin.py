# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 17:15:31 2022

@author: tapas
"""


admin_user={"Tapas": "Tapas@007"}

inventory = {1: {'Name': 'Tandoori Chicken', 'FoodID': 1,'Quantity': '4 pieces', 'Price': 240,'Discount':10, 'Stock': 30},
             2: {'Name': 'Vegan burger', 'FoodID': 2,'Quantity': '1 pieces', 'Price': 320,'Discount':10, 'Stock': 20},
             3: {'Name': 'Truffle Cake', 'FoodID': 3,'Quantity': '500 gm', 'Price': 900,'Discount':20, 'Stock': 15}}


def Add_new_food_item():
    Name = input("Enter the food name you want to add :: ")
    FoodID = max(inventory.keys())+1
    Quantity = input("Enter the quantity per portion :: ")
    price = int(input("Enter the price per portion:: "))
    Discount = int(input("Enter the percentage of discount on this particular item :: "))
    stock = int(input("Enter amount left in stock in the restaurant :: "))
    
    inventory[FoodID]={
        'Name':Name,
        'FoodID':FoodID,
        'Quantity':Quantity,
        'Price':price,
        'Discont':Discount,
        'Stock':stock
        }
    print('\n')
    print("The fooditem {} is added to the Inventory".format(Name))
    return inventory


def edit_food_item():
    i=int(input("Enter which Food item id you want to edit :: "))
    if i  not in inventory.keys():
        i=int(input("The item id does not exist ,Renter which Food item id you want to edit :: "))
    Name = input("Enter the food name you want to add :: ")
    Quantity = input("Enter the quantity per portion :: ")
    price = int(input("Enter the price per portion:: "))
    Discount = int(input("Enter the percentage of discount on this particular item :: "))
    stock = int(input(" Enter amount left in stock in the restaurant ::"))
    inventory[i]['Name'] = Name
    inventory[i]['Quantity']=Quantity
    inventory[i]['Price']=price
    inventory[i]['Discount']=Discount
    inventory[i]['Stock']=stock
    print("The food item {} is successfully edited".format(Name))
    return inventory


def view_inventory():
    print("These are the fooditems in the inventory")
    for i in inventory:
        print("{}. {} ({}) [INR {} ]".format(inventory[i]['FoodID'],inventory[i]['Name'],inventory[i]['Quantity'],inventory[i]['Price']))
    
    
def remove_food_item():
    for i in inventory:
        print(i,inventory[i])
    foodid=int(input("Enter the food id which you want to remove from the above table"))
    if foodid  not in inventory.keys():
        foodid=int(input("The item id does not exist ,Renter which Food item id you want to edit :: "))
    inventory.pop(foodid)
    print("The food item is successfully removed")
    
    