# Run with uvicorn server:apiobj --port 8000 --reload
from fastapi import FastAPI
import threading
import time
import uvicorn
import os
import json
import requests
from market import Market
from trader import Trader
from account import Account
from good import Good


apiobj = FastAPI()

#Only one market will exist
m = Market()

def thread_function():
    while(True):
        requests.get("http://localhost:8000/refresh-values")
        time.sleep(10)

#refreshes the values of each good
@apiobj.get("/refresh-values")
async def refresh():
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
    access = m.get_trader_by_id(id).validate(passw)
    return {"result" : access}

#Return the goods
@apiobj.get("/get-goods")
async def getGoods():
    marketgoods = {}
    for key,val in m.get_goods().items():
        marketgoods[key] = val.get_value()
    return marketgoods

#Buy a chosen amount of a good
@apiobj.get("/buy/{id}/{good}/{amount}")
async def buyGood(id: int, good: str, amount: int):
    m.trader_buy(id, good, amount)


if __name__ == '__main__':
    #The updater Thread continuously refreshes the values
    updater = threading.Thread(target=thread_function, args=(), daemon=True)
    updater.start()
    this_python_file = os.path.basename(__file__)[:-3]
    instance = uvicorn.run(f"{this_python_file}:apiobj", host="127.0.0.1", port=8000, log_level="info", reload=True)
