import requests
import threading
import time
from pprint import pprint as pretty_print # Für übersichtliche Textausgabe

def thread_function():
    while(True):
        requests.get("http://localhost:8000/refresh-values")
        time.sleep(10)


def lobby():
    base_api = "http://localhost:8000"
    print("Would you like to: ")
    print("Login[1]")
    print("Create a new account [2]")
    
    choice = input()
    if(choice == str(1)):
        trader_id = input("Enter your id please")
        pasw = input("Enter your password")

        #check wether password and id are compatible
        counter = 0
        while(not requests.post(base_api + "/validate/" + trader_id + "/" + pasw).json().get("result")):
            print(str(5 - counter) + " trie(s) left")
            pasw = input("Enter your password")      
            counter += 1
            if(counter == 5):
                break

    elif(choice == str(2)):
            id = requests.get(base_api + "/add-trader").json().get("trader-id")
            print("Your id is: " + str(id))
            new_pw = input("Choose your password: ")
            requests.get(base_api + "/set-password/" + str(id) + "/" + new_pw)


def main():
    #The updater Thread continuously refreshes the values
    updater = threading.Thread(target=thread_function, args=(), daemon=True)
    updater.start()

    base_api = "http://localhost:8000"

    lobby()


    
   


if __name__ == '__main__':
    main()