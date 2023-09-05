#include <trader.hpp>

namespace TradingSpace {

    //! Hashfunction to support the use of an unordered set
    size_t TraderHash::operator()(const TradingSpace::Trader& t) const {
        return std::hash<int>{}(t.get_account().get_balance());
    }

    Trader::Trader(Account& acc) {
        this->account = acc;
    }

    void Trader::buy(Good& g, int amount) {

    }

    void Trader::sell(Good& g, int amount) {

    }

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

  
}