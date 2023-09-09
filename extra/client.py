import requests
import threading
import time
from pprint import pprint as pretty_print # Für übersichtliche Textausgabe



#The login function will be called when a trader that already existed tries to access the market
def login() -> int:
    base_api = "http://localhost:8000"
    trader_id = input("Enter your id please")
    pasw = input("Enter your password")

    #check wether password and id are compatible
    counter = 0
    while(not requests.get(base_api + "/validate/" + trader_id + "/" + pasw).json().get("result")):
        print(str(5 - counter) + " trie(s) left")
        pasw = input("Enter your password")      
        counter += 1
        if(counter == 5):
            print("Your account will be deleted, you'll have to create a new one")
            delete_account(trader_id)
            break
        return id



#Create a new account and let the trader choose the password
def new_account() -> int:
    base_api = "http://localhost:8000"
    id = requests.get(base_api + "/add-trader").json().get("trader-id")
    print("Your id is: " + str(id))
    new_pw = input("Choose your password: ")
    requests.get(base_api + "/set-password/" + str(id) + "/" + new_pw)
    return id

#Delete an existing account
def delete_account(id : int):
    base_api = "http://localhost:8000"
    requests.post(base_api + "/remove-trader/" + str(id))

def print_goods():
    base_api = "http://localhost:8000"
    av_goods = requests.get(base_api + "/get-goods").json()
    for key,val in av_goods.items():
        print(key + ": " + str(round(val,2)))

def main():
    

    #The base_api is the part of the URI that will always stay the same
    base_api = "http://localhost:8000"

    print("Would you like to: ")
    print("Login[1]")
    print("Create a new account [2]") 

    choice = input()
    choice_made = False

    trader_id = ""

    #Let the trader choose wether he wants to login or create a new trading account
    while(not choice_made):
        if(choice == str(1)):
            trader_id = login()
            choice_made = True
        elif(choice == str(2)):
            trader_id = new_account()
            choice_made = True
        else:
            print("Not a valid choice")

    print("Those are the available goods")
   
    print_goods()

    print("-------------------------")
    balance = requests.get(base_api + "/balance/" + str(trader_id)).json().get("balance")
    print("Your balance is: " + str(balance))
    

    print("To refresh the prices press[1], to buy a good press[2] and to sell press [3] and to exit press [4]")
    choice = input()

    while(choice != str(4)):
        if(choice == str(1)):
            print_goods()
            choice = input()
        elif(choice == str(2)):
            good_to_buy = input("Which good would you like to buy?")
            amount = input("How many would you like to buy?")


    
   


if __name__ == '__main__':
    main()