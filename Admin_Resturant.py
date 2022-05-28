#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random

admin_keys = {'Welcome':"Welcome@123"}

inven={1:{'ItemName':'Tandoori Chiken', 'FoodID': random.randint(0,10), 'Price':240, 'Discount_Percent':10, 'Quantity':'4 pieces', 'Stock':10},
      2: {'ItemName':'Vegan Burger', 'FoodID': random.randint(10,20), 'Price':320, 'Discount_Percent':10,'Quantity':'1 pieces', 'Stock':10},
      3: {'ItemName':'Truffle Cake', 'FoodID': random.randint(20,30), 'Price':900, 'Discount_Percent':10,'Quantity':'500gms', 'Stock':5}}
print(inven)


def add_new_item():
    ItemName = input("Enter the Item name: ")
    FoodID = random.randint(30,40)
    Price = int(input("Enter the price of the item: "))
    Discount_Percent=int(input("Enter the discount amount:"))
    Quantity = input("Enter the quantity:")
    Stock = int(input("Enter the stock value of item: "))
    inven[random.randint(0,10)] = {
        "ItemName": ItemName,
        "FoodID": FoodID,
        "Price": Price,
        "Discount_Percent": Discount_Percent,
        "Quantity": Quantity,
        "Stock": Stock
    }
    print("The Item" +ItemName+ "is successfully added")
    return inven
add_new_item()

def update_stock():
    item = int(input("Enter the FoodID which you want to edit: "))
    i_name = input("Enter the item name:")
    p_price = int(input("Enter the price of item:"))
    d_discount=int(input("Enter the discount amount:"))
    q_quantity = int(input("Enter the quantity:"))
    s_stock = int(input("Enter the stock of the item:"))    
    
    inven[item]["ItemName"] = i_name
    inven[item]["Price"] = p_price
    inven[item]["Stock"] = q_quantity
    inven[item]["Discount_Percent"]=d_discount
    print("*****Stock succesfully edited*****")
    return inven
update_stock()


def display_invent():
    print("*****HERE IS THE INVENTORY OF ABC RESTURANT*****")
    for i in inven:
        print("Item Name: ",inven[i]["ItemName"])
        print("Food ID: ",inven[i]["FoodID"])
        print("Price:", inven[i]["Price"] - inven[i]["Discount_Percent"]* inven[i]["Price"]/100,"INR")
        print("Quantity:",inven[i]["Quantity"])
        print("Stock:",inven[i]["Stock"])        
display_invent()

def remove_item():
    d = int(input("Enter the Item id which you want to remove"))
    inven.pop(d)
    print("Remove item successfully removed from the stock ")
    return inven
remove_item()


# In[ ]:




