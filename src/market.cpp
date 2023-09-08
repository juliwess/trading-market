#include <market.hpp>
#include <chrono>
#include <thread>
#include <iostream>

namespace TradingSpace {

    Market::Market() {
        Good bricks(1, "Bricks", 1, 1.2, 0.5, 0.7);
        Good oil(2, "Oil", 10, 0.2, 0.5, 0.3);
        Good wood(3,"Wood", 5, 1.8, 0.5, 0.9);
        Good iron(4,"Iron", 3, 1.6, 0.5, 0.1);
        Good gas(5,"Gas", 0.5, 0.6, 0.5, 0.2);
        Good chemicals(6,"Chemicals", 15, 1.2, 0.5, 0.8);

        goods.insert({"Bricks", bricks});
        goods.insert({"Oil",oil});
        goods.insert({"Wood", wood});
        goods.insert({"Iron", iron});
        goods.insert({"Gas", gas});
        goods.insert({"Chemicals", chemicals});
    }

    void Market::addTrader(Trader& trader) {
        traders.insert({trader.get_id(), trader});
    }

    void Market::removeTrader(Trader& trader) {
        traders.erase(trader.get_id());
    }   

    void Market::removeTraderById(int id) {
        traders.erase(id);
    }

    void Market::update_values() {
        for(auto& [first,second] : goods) {
            second.adapt();
        }
    }


    /**
     * GETTER AND SETTER
    */

    std::unordered_map<int, Trader>& Market::get_traders() {
        return traders;
    }

    std::unordered_map<std::string, Good>& Market::get_goods()  {
        return goods;
    }

    void Market::set_trader_password(int id, std::string pw) {
        get_traders().at(id).set_pw(pw);
    }

    Trader& Market::get_trader_by_id(int id) {
        return traders.at(id);
    }
    /**
     * GETTER AND SETTER
    */




} // namespace TradingSpace
