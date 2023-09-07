# Run with uvicorn server:apiobj --port 8000 --reload
from fastapi import FastAPI
from market import Market
from trader import Trader
from account import Account
from good import Good


apiobj = FastAPI()

m = Market()


@apiobj.get("/")
async def wurzel_pfad():
    return {"coole_nachricht" : "Fast API funktioniert"}

@apiobj.get("/add-trader")
async def addTrader():
    t = Trader()
    m.addTrader(t)
    print(m.get_traders())
    return {"trader-id" : t.get_id()}


@apiobj.get("/user/{id}")
async def get_current_user(id: int):
    return {"trader-id" : m.get_traders().get(id).get_name()}

@apiobj.get("/remove-trader/{id}")
async def printtraders(id: int):
    m.removeTraderById(id)
    print(m.get_traders())
    return{"trader-id" : id}