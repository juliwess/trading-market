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
    void Trader::buy(const Good& g, int amount) {

        float cost = amount * g.get_value();

        //Does the trader posses enough coins to buy the intended amount?
        if(cost <= get_account().get_balance()) {
            
            get_account().withdraw(amount * g.get_value());
            //Insert the good if it doesen't exist already and update the amount
            int count = traders_goods.count(g.get_name());
            if(count == 0) {
                traders_goods.insert({g.get_name(), amount});
            } else {
                int old_amount = traders_goods.at(g.get_name());
                int new_amount = old_amount + amount;
                traders_goods.insert_or_assign(g.get_name(), new_amount);
            }
        }
    }

    void Trader::sell(const Good& g, int amount) {

        int old_amount = traders_goods.at(g.get_name());
        int new_amount = old_amount - amount;

        //Does the trader posses enough to sell the requested amount?
        if(new_amount > 0) {
            traders_goods.insert_or_assign(g.get_name(), new_amount);
            get_account().deposit(amount * g.get_value());
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

    std::unordered_map<std::string, int>& Trader::get_traders_goods() {
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