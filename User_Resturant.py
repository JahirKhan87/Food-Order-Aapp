#!/usr/bin/env python
# coding: utf-8

# In[18]:


import Admin_Resturant as rest

class User:
    login_info = {"Resturant": "Resturant@123"}
    profile={}
    def __init__(self):
        self.name = input('Enter your name:')
        self.number = input('Enter your phoneno:')
        self.email = input('Enter your email:')
        self.address = input('Enter your address:')
        self.password = input ('Enter your password:')
        User.login_info[self.name] = self.password
        self.order_history = {}

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("You're are successfully logged in.....")
            return True
        else:
            print("SORRY! Wrong credentials entered")
            return False
         
    def user_profile(self):
        self.profile= {"Name":self.name, "Number":self.number,"Email":self.email, "Address":self.address, "password":self.password}
        
    def display(self):
        print(self.profile)
        
    def update_profile(self):
        self.profile["name"] = input('Enter your name to update:')
        self.profile["number"] = input('Enter your number to update:')
        self.profile["email"] = input('Enter your email to update:')
        self.profile["address"] = input('Enter your address to update:')
        return self.profile     


    def place_order(self):
        print("What you want to order here in the Inventory")
        print(rest.display_invent())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            n=int(input("Enter how many items do you want to Order"))
            x=0
            for i in range(n):
             
             FoodID = int(input("Enter the Food ID here: "))
             qunty = int(input("Enter the quantity of the item: "))
             x += rest.inven["FoodID"]["Price"] * qunty
            again_ask = input("Are you still want to order this Enter YES or NO")
            if again_ask == "YES":
                print(f'''Your item name is {rest.inven["FoodID"]["ItemName"]}''')
                print(f'''Price of your Item is {rest.inven["FoodID"]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.order_history["FoodID"] = {
                    "Item Name": rest.inven["FoodID"]["ItemName"],
                    "Price": rest.inven["FoodID"]["Price"],
                    "Quantity": qunty
                }
                final_stock = rest.inven["FoodID"]["Stock"] - qunty
                rest.inven["FoodID"]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")
    
p1=User()
p1.user_profile()
p1.place_order()
p1.display()
p1.update_profile() 
    



# In[ ]:





# In[ ]:




