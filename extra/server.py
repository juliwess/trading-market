# Run with uvicorn server:apiobj --port 8000 --reload
from fastapi import FastAPI
import threading
import time
import uvicorn
import os
import json
import pandas
import requests
import csv
from market import Market
from trader import Trader
from account import Account
from good import Good


apiobj = FastAPI()

#Only one market will exist
m = Market()

def updater():
    while(True):
        base_api = "http://localhost:8000"
        requests.get(base_api + "/refresh-values")
        print("Worked")
        time.sleep(5)

#refreshes the values of each good
@apiobj.get("/refresh-values")
async def refresh():
    #Write the current value of all goods in a csv sheet
    # with open('GUI/values.csv', 'w', newline='') as csvfile:
    #         spamwriter = csv.writer(csvfile, delimiter=',',
    #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
    #         for key,value in m.get_goods().items():
    #             spamwriter.writerow([value.get_value()])

    df = pandas.DataFrame()
    index = 0
    for key,value in m.get_goods().items():    
        df.insert(index, key, [value.get_value()])
        index +=1

    df.to_csv("GUI/values.csv", index=False)
   



    m.update_values()
    for key,value in m.get_traders().items():
        print(str(key) + str(value.get_pw()))
    return {"status" : "success" }

#add a trader
@apiobj.get("/add-trader")
async def addTrader():
    t = Trader()
    m.addTrader(t)
    print(m.get_traders())
    return {"trader-id" : t.get_id()}

#remove a trader
@apiobj.get("/remove-trader/{id}")
async def remove(id: int):
    m.removeTraderById(id)  
    print(m.get_traders())
    return{"trader-id" : id}

#get a trade with his user-id
@apiobj.get("/balance/{id}")
async def getBalance(id: int):
    balance = m.get_traders_balance(id)
    return {"balance": balance}

#set password
@apiobj.get("/set-password/{id}/{passw}")
async def new_pw(id: int, passw: str):
    m.set_trader_password(id, passw)
    return {"password" : m.get_traders().get(id).get_pw()}

#check wether a password and an id fit together
@apiobj.get("/validate/{id}/{passw}")
async def val(id: int, passw: str):
    try:
        access = m.get_trader_by_id(id).validate(passw)
    except IndexError as e:
        access = None
    
    
    return {"result" : access}

#Return the goods
@apiobj.get("/get-goods")
async def getGoods():
    marketgoods = {}
    for key,val in m.get_goods().items():
        marketgoods[key] = val.get_value()
    return marketgoods

@apiobj.get("/get-biggest-value")
async def getBiggestValue():
    val = 0
    for key,valu in m.get_goods().items():
        if valu.get_value() > val:
            val = valu.get_value()
    print(val)
    return {"value" : float(val)}

#Return a dictinoary of the goods in the traders posession
@apiobj.get("/get-traders-goods/{id}")
async def getTradersGoods(id: int):
    t = m.get_trader_by_id(id)
    
    return t.get_traders_goods()

#Buy a chosen amount of a good
@apiobj.post("/buy/{id}/{good}/{amount}")
async def buyGood(id: int, good: str, amount: int):
    m.trader_buy(id, good, amount)

#Sell a chosen amount of a good
@apiobj.post("/sell/{id}/{good}/{amount}")
async def sell(id: int, good: str, amount: int):
    m.trader_sell(id, good, amount)


if __name__ == '__main__':
    
    
    this_python_file = os.path.basename(__file__)[:-3]
    instance = uvicorn.run(f"{this_python_file}:apiobj", host="127.0.0.1", port=8000, log_level="info", reload=True)
