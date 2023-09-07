#include <market.hpp>
#include <good.hpp>
#include <trader.hpp>
#include <account.hpp>
#include <iostream>
#include <set>
#include <functional>
#include <thread>
#include <chrono>


int main() {

    /**
     * A simple demonstration of how the classes work
    */
    TradingSpace::Market m;
    TradingSpace::Trader julian;

    //! Add one new trader and setup a balance
    m.addTrader(julian);
    julian.get_account().set_balance(1000);

    //! Setup 5 trading-cycles
    for(int i = 0; i <= 5; i++) {
        std::cout<<"Your coins: "<<julian.get_account().get_balance()<<"$"<<std::endl;

        std::cout<<"Would you like to buy[1] or sell[2]?"<<std::endl;
        int in;
        std::cin>>in;

        std::cout<<"------------------"<<std::endl;
        std::cout<<"Available goods"<<std::endl;
        //Print the goods and their values
        for(auto& [first,second] : m.get_goods()){
            std::cout<< first <<": " << second.get_value() <<"$"<<std::endl;
        }

        std::cout<<"------------------"<<std::endl;
        std::cout<<"Your goods"<<std::endl;

        //Print the goods in posession
        for(auto& [first,second] : m.get_goods()){
            if(julian.get_traders_goods().count(first) == 1){
                std::cout<< first <<": " << julian.get_traders_goods().at(first)<<std::endl;
            }else {
                std::cout<< first <<": " << 0<<std::endl;
            }
        }

        //Simple yes/no -logic to demonstrate the proscedure 
        if(in == 1) {
            std::cout<<"------------------"<<std::endl;
            std::cout<<"Enter the name of the good you'd like to buy"<<std::endl;
            std::string name;
            std::cin>>name;
            std::cout<<"Enter the amount you'd like to buy"<<std::endl;
            int amount;
            std::cin>>amount;
            julian.buy(m.get_goods().at(name), amount);
            m.update_values();
        }

        if(in == 2 ) {
            std::cout<<"------------------"<<std::endl;
            std::cout<<"Enter the name of the good you'd like to sell"<<std::endl;
            std::string name;
            std::cin>>name;
            std::cout<<"Enter the amount you'd like to sell"<<std::endl;
            int amount;
            std::cin>>amount;
            julian.sell(m.get_goods().at(name), amount);
            m.update_values();
        }
    }
}