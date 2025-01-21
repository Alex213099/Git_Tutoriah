"""
Author:Alex Gitonga
last date modified:10/01/2024

"""
#continue on this program on moday .also include git to track changes.THankyou. and may the grace of God be in us.Adios.

balance=2000
pin=1234


def update_balance(balance,method):
    if method==deposit:
        return balance
    
    """elif send_money():
        balance-=amount
        return amount
    elif check_balance():
        return balance
    elif withdraw():
        balance-=amount
        return balance"""


pin=1234
    

def display_options():
    print("1 . Deposit")
    print("2 . send Money")
    print("3 .check balance")
    print("4. withdraw")


def get_input(balance):

    value=int(input("Enter your choice please: "))
    
    if isinstance(value,int):

        while value <=0 or value >4:
            value=int(input("Enter your choice please: "))
        
        if value==1:
            deposit(balance)
        elif value==2:
            send_money(balance)
        elif value==3:
            check_balance(balance)
        elif value==4:
            withdraw(balance)
        else:
            raise Exception("wrong input")
    else:
        print("enter a valid entry")
        get_input(balance)
    return value

def transaction_cost(am_get,balance):
    if am_get >100 and am_get <500 :
        transaction_cost=1.5
        balance-=am_get+am_get*transaction_cost/100
        return balance
    elif am_get >=500 and am_get <1000:
        transaction_cost=2.5
        am_get=am_get+am_get*transaction_cost/100
        balance-=am_get
        return balance
    elif am_get <=100:
        transaction_cost=0
        am_get=am_get+am_get*transaction_cost/100
        balance-=am_get
        return balance
        
    else:
        transaction_cost=3.0 
        am_get=am_get+am_get*transaction_cost/100
        balance-=am_get
        return balance
    
def enter_pin(pin):
    Entered_pin=int(input("Enter Your pin: "))
    if pin==Entered_pin:
        return True 
    else:
        print("You entered the wrong pin. Kindly Try again ")
        enter_pin(pin)

def deposit(balance):
    method=deposit
    amount=float(input("Enter amount to deposit: "))
    result_of_pin=enter_pin(pin)
    if result_of_pin== True:
        balance+=amount
        print(f"succesfully deposited {amount} .Total account balance is {balance}")
        update_balance(balance,amount,method)
    else:
        pass
   

def send_money(balance):
    #recepient=input("Phone Number: ")

    amount=float(input("Enter amount you want to send "))
    result_of_pin=enter_pin(pin)
    if result_of_pin ==True:
        if amount>balance:
            print("you have insuffient balance")
        else: 
            new_balance=transaction_cost(amount,balance)
            print(f"confirmed {amount} sent new balance is {new_balance}")
            update_balance()
    else:
        pass

 
def check_balance(balance):
    result_of_pin =enter_pin(pin)
    if result_of_pin==True:
        print(f"your balance is {balance} Transaction cost ksh 00")
        update_balance()
    else:
        pass

def withdraw(balance):
    amount=float(input("Enter amount to withdraw "))
    result_of_pin=enter_pin(pin)
    if result_of_pin ==True:
        if amount>balance:
            print("insufficient balance")
        else:
            new_balance=transaction_cost(amount,balance)
            print(f"succesfully withdrawn {amount} new balance is {new_balance}")
            update_balance()
    else:
        pass

display_options(balance)
get_input(balance)
"""if __name__=="main()":
    display_options()
    get_input(balance)
"""

