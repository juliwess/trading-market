#include <trader.hpp>
#include <iostream>

namespace TradingSpace {

    //! Hashfunction to support the use of an unordered set
    size_t TraderHash::operator()(const TradingSpace::Trader& t) const {
        return std::hash<int>{}(t.get_id());
    }

    //! The global variable is used to give every trader a unique id
    int Trader::instances = 0;

    Trader::Trader() {
        Account acc;
        account = acc;
        id = instances;
        instances += 1;
    }

    /**
     * Buy and sell Goods
    */
    void Trader::buy(Good& g, int amount) {

        float cost = amount * g.get_value();

        //Does the trader posses enough coins to buy the intended amount?
        if(cost < get_account().get_balance()) {

            //Insert the good if it doesen't exist already and update the amount
            int count = traders_goods.count(g);
            if(count == 0) {
                traders_goods.insert({g, amount});
            } else {
                int old_amount = traders_goods.at(g);
                int new_amount = old_amount + amount;
                traders_goods.insert_or_assign(g, new_amount);
            }
        }
    }

    void Trader::sell(Good& g, int amount) {

        int old_amount = traders_goods.at(g);
        int new_amount = old_amount - amount;

        if(new_amount > 0) {
            traders_goods.insert_or_assign(g, new_amount);
        }
    }
    /**
     * GETTER AND SETTER
    */
    Account& Trader::get_account(){
        return account;
    }

    void Trader::set_account(Account& acc) {
        account = acc;
    }

    int Trader::get_id() const{
        return id;
    }

    void Trader::set_id(int& id) {
        this->id = id;
    }

    int Trader::get_instances() const {
        return instances;
    }

    std::unordered_map<Good, int, GoodHash> Trader::get_traders_goods() const {
        return traders_goods;
    }
    /**
     * GETTER AND SETTER
    */

    //! Compare operator for unordered set
    bool Trader::operator==(const Trader& other) const {
        return id == other.get_id();
    }

  
}