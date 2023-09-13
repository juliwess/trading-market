#include <market.hpp>
#include <chrono>
#include <thread>
#include <iostream>
#include <fstream>
#include <cstdlib>

namespace TradingSpace {

    

    //!The constructor adds the goods and their start values to the market
    Market::Market() {
        //!Generate random values for the goods random walk
        float r = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r2 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r3 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r4 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r5 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r6 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r7 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r8 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r9 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r10 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r11 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
        float r12 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));

        Good bricks(1, "Bricks", 1, r, 0.5, r2);
        Good oil(2, "Oil", 7, r3, 0.5, r4);
        Good wood(3,"Wood", 5, r5, 0.5, r6);
        Good iron(4,"Iron", 3, r7, 0.5, r8);
        Good gas(5,"Gas", r9, 0.6, 0.5, r10);
        Good chemicals(6,"Chemicals", 15, r11, 0.5, r12);

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
