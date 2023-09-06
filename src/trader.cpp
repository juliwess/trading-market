#include <trader.hpp>

namespace TradingSpace {

    //! Hashfunction to support the use of an unordered set
    size_t TraderHash::operator()(const TradingSpace::Trader& t) const {
        return std::hash<int>{}(t.get_id());
    }

    //! The global variable is used to give every trader a unique id
    int Trader::instances = 0;

    Trader::Trader(Account& acc) {
        this->account = acc;
        id = instances;
        instances += 1;
    }

    /**
     * Buy and sell Goods
    */
    void Trader::buy(Good& g, int amount) {

    }

    void Trader::sell(Good& g, int amount) {

    }
    /**
     * GETTER AND SETTER
    */
    Account Trader::get_account()const {
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
    /**
     * GETTER AND SETTER
    */

    //! Compare operator for unordered set
    bool Trader::operator==(const Trader& other) const {
        return id == other.get_id();
    }

  
}