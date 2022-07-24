# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 17:16:16 2022

@author: tapas
"""

import admin as ad
from user import user

uhh = user(str, int, str, str, str)

inputt= int(input("Enter a number 1:Admin 2:user 3:exit"))
if inputt==1:
    print("Welcome to the admin panel")
    username = input("Enter the username ::")
    password = input("enter the password ::")
    if ad.admin_user[username]==password:
        print('________________________________________________________________')
        print("**********You are successfully logged in as admin user**********")
        print('________________________________________________________________')
        admin_crawler = True
        while admin_crawler:
            s = int(input('Enter an option \n 1:Add new food item \n 2:edit food item \n 3:view inventory \n 4:remove food item  \n 5:exit \n'))
            if s==1:
                ad.Add_new_food_item()
            elif s==2:
                ad.edit_food_item()
            elif s==3:
                ad.view_inventory()
            elif s==4:
                ad.remove_food_item()
            elif s==5:
                print("{}, You are logged out ".format(username))
                admin_crawler=False
            else:
                print("Please select the wright option ")
    else:
        print("The username and passwords is incorrect")
            
elif inputt==2:
    print('___________________________________________________________________')
    print("*********************WELCOME TO THE USER PANEL*********************")
    print('___________________________________________________________________')
    fullname=input("Enter your name :: ")
    phonenumber=int(input("Enter your phone number :: "))
    email = input("Enter your email id :: ")
    address=input("Enter your address :: ")
    username=input("Enter a user name :: ")
    while username in user.login_info.keys():
        print("Please try another username , this username is already existed")
        username=input("Enter a new user name :: ")
    password=input("Enter your password :: ")
    
    
    if user.signup(fullname,phonenumber,email,address,username,password):
        print('___________________________________________________________________')
        print("***********************WELCOME TO THE LOGIN PANEL**********************")
        print('___________________________________________________________________')
        username = input("Enter your username :: ")
        password = input("Enter your password:: ")
        if user.login(username, password):
            print("Done.........")
            user_crawler=True
            while user_crawler:
                user_choice = int(input("Please enter a choice \n 1:Place new order \n 2:order history \n 3:update profile \n 4:exit \n"))
                if user_choice==1:
                    uhh.place_new_order(username)
                if user_choice==2:
                    uhh.order_history_(username)
                if user_choice==3:
                    uhh.update_profile(username)
                if user_choice==4:
                    print("Thank you for shopping with us .")
                    user_crawler = False
else:
    print("Thank you ! Visit again")
    
    