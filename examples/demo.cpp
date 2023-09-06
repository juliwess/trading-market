#include <market.hpp>
#include <good.hpp>
#include <trader.hpp>
#include <account.hpp>
#include <iostream>
#include <set>
#include <functional>



int main() {
    TradingSpace::Account a;
    TradingSpace::Trader t(a);
    TradingSpace::Trader c(a);
    TradingSpace::Trader d(a);
    TradingSpace::Trader e(a);

    TradingSpace::Market m;
    m.addTrader(t);
    m.addTrader(c);
    m.addTrader(d);
    m.addTrader(e);

    for(const auto& in : m.get_traders()) {
        std::cout<<in.get_id();
    }

}