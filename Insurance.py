def add_customer():

    cust_id=input("Enter Customer ID: ")
    name=input("Enter Name: ")
    phone=input("Enter Phone: ")
    location=input("Enter Location: ")

    file=open("customers.txt","a")
    file.write(f"{cust_id},{name},{phone},{location}\n")

    print("Customer added successfully")

    file.close()


# Create required files automatically
open("customers.txt","a").close()
open("policies.txt","a").close()
open("payments.txt","a").close()
open("claims.txt","a").close()

import random


def display_customers():

    print("CUSTOMERS")
    print("----------------")

    file=open("customers.txt","r")
    print(file.read())
    file.close()

def add_policy():

    policy_id=input("Enter Policy ID: ")
    cust_id=input("Enter Customer ID: ")
    policy_type=input("Enter Policy Type (Health/Life/Vehicle): ")
    premium=input("Enter Premium Amount: ")

    file=open("policies.txt","a")
    file.write(f"{policy_id},{cust_id},{policy_type},{premium}\n")

    print("Policy created successfully")

    file.close()

def display_policies():

    print("POLICIES")
    print("----------------")

    file=open("policies.txt","r")
    print(file.read())
    file.close()

import random

def display_payments():

    print("PAYMENTS")
    print("----------------")

    file=open("payments.txt","a+")
    file.seek(0)
    print(file.read())
    file.close()

def display_payments():

    print("PAYMENTS")
    print("----------------")

    file=open("payments.txt","r")
    print(file.read())
    file.close()

def raise_claim():

    claim_id=input("Enter Claim ID: ")
    policy_id=input("Enter Policy ID: ")
    amount=input("Enter Claim Amount: ")

    file=open("claims.txt","a")

    file.write(f"{claim_id},{policy_id},{amount},PENDING\n")

    print("Claim raised successfully")

    file.close()

def display_claims():

    print("CLAIMS")
    print("----------------")

    file=open("claims.txt","r")
    print(file.read())
    file.close()

import random

def pay_premium():

    cust_id=input("Enter Customer ID: ")
    policy_id=input("Enter Policy ID: ")
    amount=input("Enter Payment Amount: ")

    payment_id=random.randint(1000,9999)

    file=open("payments.txt","a")

    file.write(f"{payment_id},{cust_id},{policy_id},{amount},PAID\n")

    print("Premium payment successful")

    file.close()

def display_payments():

    print("PAYMENTS")
    print("----------------")

    file=open("payments.txt","r")
    print(file.read())
    file.close()

def admin_menu():

    print("\nADMIN MENU")
    print("1 Add Customer")
    print("2 Display Customers")
    print("3 Add Policy")
    print("4 Display Policies")
    print("5 View Payments")
    print("6 View Claims")

    choice=int(input("Enter choice: "))

    if choice==1:
        add_customer()

    elif choice==2:
        display_customers()

    elif choice==3:
        add_policy()

    elif choice==4:
        display_policies()

    elif choice==5:
        display_payments()

    elif choice==6:
        display_claims()

def customer_menu():

    print("\nCUSTOMER MENU")
    print("1 View Policies")
    print("2 Pay Premium")
    print("3 Raise Claim")

    choice=int(input("Enter choice: "))

    if choice==1:
        display_policies()

    elif choice==2:
        pay_premium()

    elif choice==3:
        raise_claim()

def run():

    print("INSURANCE MANAGEMENT SYSTEM")

    print("1 Admin")
    print("2 Customer")

    choice=int(input("Enter choice: "))

    if choice==1:
        admin_menu()

    elif choice==2:
        customer_menu()

run()
