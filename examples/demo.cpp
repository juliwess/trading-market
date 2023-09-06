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
    TradingSpace::Market m;
    TradingSpace::Trader julian;


    m.addTrader(julian);
    julian.get_account().set_balance(1000);
    julian.buy(m.get_goods().at("Oil"),2);

    for(int i = 0; i <= 3; i++) {
        std::cout<<"Your coins: "<<julian.get_account().get_balance()<<"$"<<std::endl;

        std::cout<<"Would you like to buy[1] or sell[2]?"<<std::endl;
        int in;
        std::cin>>in;

        std::cout<<"------------------"<<std::endl;
        std::cout<<"Available goods"<<std::endl;
        for(auto& [first,second] : m.get_goods()){
            std::cout<< first <<": " << second.get_value() <<"$"<<std::endl;
        }

        std::cout<<"------------------"<<std::endl;
        std::cout<<"Your goods"<<std::endl;
        for(auto& [first,second] : m.get_goods()){
            if(julian.get_traders_goods().count(first) == 1){
                std::cout<< first <<": " << julian.get_traders_goods().at(first)<<std::endl;
            }else {
                std::cout<< first <<": " << 0<<std::endl;
            }
        }

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