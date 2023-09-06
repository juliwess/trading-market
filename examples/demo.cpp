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
    
    auto& g = m.get_goods();
    
    for(int i=0; i<= 30; i++) {
        for(auto& [first, second]: g) {
            std::cout << first << ": " << second.get_value() << "\n";
            second.adapt();
        }
        std::cout<<"\n";
    }
    

 
    

    

}