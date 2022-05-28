#!/usr/bin/env python
# coding: utf-8

# In[4]:


import Admin_Resturant as auth
from User_Resturant import User

uhh = User(str, str, str, str, str)

option = int(input("Where You want to login select 1.Admin and 2.User and 3.Exit"))
if option == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if auth.admin_keys[Username] == Password:
        print("*****You're successfully logged inn*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW INVENTORY 4.REMOVE ITEM 5.EXIT"))
            if adm_choice == 1:
                auth.add_new_item()
            elif adm_choice == 2:
                auth.edit_from_item()
            elif adm_choice == 3:
                auth.show_inven()
            elif adm_choice == 4:
                auth.remove_item()
            elif adm_choice == 5:
                print(f"You're Exit to the admin panel{Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
elif option == 2:
    print("Welcome to the user panel of ABC Resturant")
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
        print(f"You are logged in successfully {username}")
        user_crawler = True
        while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history 3.Exit"))
            if usr_choice == 1:
                uhh.place_order()
            elif usr_choice == 2:
                print(f"Here is your order history, {username}")
                print(uhh.order_history)
            elif usr_choice == 3:
                user_crawler = False
                print("You're Successfully looged out")
            else:
                print("You choose the invalid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
else:
    exit()



# In[ ]:




