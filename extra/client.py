import requests
import threading
import time
import json
from pprint import pprint as pretty_print # Für übersichtliche Textausgabe



#The login function will be called when a trader that already existed tries to access the market
def login() -> int:
    base_api = "http://localhost:8000"
    
    #A trader id must always contain at least one character
    trader_id = ""
    while(trader_id == ""):
        trader_id = input("Enter your ID please")

        #Did the trader enter something that is not a number?
        try:
            int(trader_id)
        except ValueError as e:
            trader_id = ""
            print("Invalid")
    
    #A password cant't be empty
    pasw = ""
    while(pasw == ""):
            pasw = input("Enter your password")

    #If the result can't be fetched the ID must be invalid
    try:
        requests.get(base_api + "/validate/" + trader_id + "/" + pasw).json().get("result")
        
    except json.decoder.JSONDecodeError as e:
        print("Invalid trader_id! Please try again")
        login()

    #check wether password and id are compatible
    counter = 0
    
    # You've got 5 tries to login the loop only runs if you have a low enough amount of tries and enter the wrong password
    while(not requests.get(base_api + "/validate/" + str(trader_id) + "/" + str(pasw)).json().get("result") and counter != 5):
       print("Wrong password")
       print(str(5 - counter) + " try/tries left")
       counter += 1
       pasw = input("Try again: ")
       print(requests.get(base_api + "/validate/" + str(trader_id) + "/" + str(pasw)).json().get("result"))
       
       #Right pw entered?
       if(requests.get(base_api + "/validate/" + str(trader_id) + "/" + str(pasw)).json().get("result")):
        return trader_id
    
    # Right pw entered?
    if(requests.get(base_api + "/validate/" + str(trader_id) + "/" + str(pasw)).json().get("result")):
        return trader_id
    
    #if a trader enters faulty too many times his account will be removed
    print("Too many false tries, your account will be deleted")
    requests.get(base_api + "/remove-trader/" +str(trader_id))
    return trader_id



#Create a new account and let the trader choose the password
def new_account() -> int:
    base_api = "http://localhost:8000"
    id = requests.get(base_api + "/add-trader").json().get("trader-id")
    print("Your id is: " + str(id))
    new_pw = ""
    while(new_pw == ""):
        new_pw = input("Choose your password: ")
    requests.get(base_api + "/set-password/" + str(id) + "/" + new_pw)

    return id

#Delete an existing account
def delete_account(id : int):
    base_api = "http://localhost:8000"
    requests.post(base_api + "/remove-trader/" + str(id))

#Basic print functions
#
#
def print_goods():
    base_api = "http://localhost:8000"
    av_goods = requests.get(base_api + "/get-goods").json()
    for key,val in av_goods.items():
        print(key + ": " + str(round(val,2)) + "$")

def print_traders_goods(trader_id: int):
    base_api = "http://localhost:8000"
    traders_goods = requests.get(f"{base_api}/get-traders-goods/{trader_id}").json()
    for key,val in traders_goods.items():
        print(f"{key}: {val}")

def print_balance(trader_id: int):
    base_api = "http://localhost:8000"
    balance = requests.get(base_api + "/balance/" + str(trader_id)).json().get("balance")
    print(f"Your balance: {balance}$")

#
#
#Basic print functions

def updater():
    while(True):
        base_api = "http://localhost:8000"
        requests.get(base_api + "/refresh-values")
        print("Worked")
        time.sleep(5)

def main():
    
    update_thread = threading.Thread(target=updater, daemon=True)
    update_thread.start()

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
            choice_made = input("Enter again: ")
    
    #Print the traders balance
    print("-------------------------")
    print_balance(trader_id)

    print("Your goods: ")
    print_traders_goods(trader_id)

    #Print the available goods
    print("-------------------------")
    print("Those are the prices for the goods")
   
    print_goods()

    
    

    choice = input("[1]Refresh the prices press [2]buy a good [3] sell [4]display goods [5]exit")

    #Runs as long as the trader doesn't decide to exit
    while(choice != str(5)):
        #print the goods
        if(choice == str(1)):
            print_goods()
            choice = input("[1]Refresh the prices press [2]buy a good [3] sell [4]display goods [5]exit")
        #buy something
        elif(choice == str(2)):
            good_to_buy = input("Which good would you like to buy?")
            amount = input("How many would you like to buy?")
            requests.post(f"{base_api}/buy/{trader_id}/{good_to_buy}/{amount}")
            balance = requests.get(base_api + "/balance/" + str(trader_id)).json().get("balance")
            print(f"Your balance: {round(balance, 2)}$")
            choice = input("[1]Refresh the prices press [2]buy a good [3] sell [4]display goods [5]exit")
        #sell something
        elif(choice == str(3)):
            good_to_buy = input("Which good would you like to sell")
            amount = input("How many would you like to sell?")
            requests.post(f"{base_api}/sell/{trader_id}/{good_to_buy}/{amount}")
            balance = requests.get(base_api + "/balance/" + str(trader_id)).json().get("balance")
            print(f"Your balance: {round(balance, 2)}$")
            choice = input("[1]Refresh the prices press [2]buy a good [3] sell [4]display goods [5]exit")
        #show balance
        elif(choice == str(4)):
            print_traders_goods(trader_id)
            balance = requests.get(base_api + "/balance/" + str(trader_id)).json().get("balance")
            print(f"Your balance: {round(balance, 2)}$")
            choice = input("[1]Refresh the prices press [2]buy a good [3] sell [4]display goods [5]exit")
    
   


if __name__ == '__main__':
    main()