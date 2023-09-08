# Run with uvicorn server:apiobj --port 8000 --reload
from fastapi import FastAPI
from market import Market
from trader import Trader
from account import Account
from good import Good


apiobj = FastAPI()

#Only one market will exist
m = Market()

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
@apiobj.get("/trader/{id}")
async def getTrader(id: int):
    return {"trader-id" : m.get_trader_by_id(id).get_name()}



#set password
@apiobj.get("/set-password/{id}/{passw}")
async def new_pw(id: int, passw: str):
    m.set_trader_password(id, passw)
    return {"password" : m.get_traders().get(id).get_pw()}

@apiobj.get("/validate/{id}/{passw}")
async def val(id: int, passw: str):
    access = m.get_trader_by_id(id).validate(passw)
    return {"result" : access}