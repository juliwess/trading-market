from market import Market
from trader import Trader
from good import Good
from account import Account


#A simple demonstration of the functionality of the classes in python
def main():
    #Create an object of the main classes
    m = Market()
    julian = Trader()
    julian.deposit(100)

    #10 Rouncs of trading
    for i in range (10):
        print('Your coins: ' + str(julian.get_account().get_balance())+'$ \n')
        inp: int = input('Would you like to buy[1] or sell[2]?')

        print('-----------------')
        print('Available goods: ')

        #iterate through the dictionary and print the goods and their values
        for key,value in m.get_goods().items():
            print(key + ' ' + str(value.get_value()))
        
        print('-----------------')
        print('Your goods: ')
       
       #iterate through the dictionary of goods and check wether the trader already posseses any of them
        for key,value in m.get_goods().items():
            if(julian.get_traders_goods().get(key) != None):
                print(key + ': ' + str(julian.get_traders_goods().get(key)))
            else:
                print(key + ': ' + str(0))
        
        #Buying/Selling depending on the traders choice
        if(inp == str(1)):
            print('-----------------')
            name: str = input("Enter the name of the good you'd like to buy")
            amount: int = input("Enter the amount you'd like to buy")
            julian.buy(m.get_goods().get(name), int(amount))
            m.update_values()
        if(inp == str(2)):
            print('-----------------')
            name: str = input("Enter the name of the good you'd like to sell")
            amount: int = input("Enter the amount you'd like to sell")
            julian.sell(m.get_goods().get(name), int(amount))
            m.update_values()



if __name__ == '__main__':
    main()