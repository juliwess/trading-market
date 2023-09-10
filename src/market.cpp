#include <market.hpp>
#include <chrono>
#include <thread>
#include <iostream>
#include <fstream>

namespace TradingSpace {

    //!The constructor adds the goods and their start values to the market
    Market::Market() {
        Good bricks(1, "Bricks", 1, 1.2, 0.5, 0.7);
        Good oil(2, "Oil", 7, 0.2, 0.5, 0.3);
        Good wood(3,"Wood", 5, 0.45, 0.5, 0.4);
        Good iron(4,"Iron", 3, 0.36, 0.5, 0.1);
        Good gas(5,"Gas", 0.5, 0.6, 0.5, 0.2);
        Good chemicals(6,"Chemicals", 15, 1.2, 0.5, 0.8);

        goods.insert({"Bricks", bricks});
        goods.insert({"Oil",oil});
        goods.insert({"Wood", wood});
        goods.insert({"Iron", iron});
        goods.insert({"Gas", gas});
        goods.insert({"Chemicals", chemicals});
    }

    //!Add a trader to the market
    void Market::addTrader(Trader& trader) {
        trader.set_balance(20.0F);
        traders.insert({trader.get_id(), trader});
    }

    //!Remove a trader from the market
    void Market::removeTrader(Trader& trader) {
        traders.erase(trader.get_id());
    }   

    //!Remove a trader from the market using his id
    void Market::removeTraderById(int id) {
        traders.erase(id);
    }

    //!Update the values
    void Market::update_values() {
        for(auto& [first,second] : goods) {
            second.adapt();
        }
    }

    //! Let a trader buy a good of his choice 
    void Market::trader_buy(int id, std::string good_name, int amount){
        Trader& t = traders.at(id);
        t.buy(goods.at(good_name), amount);
    }

    //! Let a trader sell a good of his choice
    void Market::trader_sell(int id, std::string good_name, int amount) {
        Trader& t = traders.at(id);
        t.sell(goods.at(good_name), amount);
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

    float Market::get_traders_balance(int id) {
        return traders.at(id).get_account().get_balance();
    }
    /**
     * GETTER AND SETTER
    */




} // namespace TradingSpace
