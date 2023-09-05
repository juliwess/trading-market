#pragma once
#include <account.hpp>
#include <good.hpp>

namespace TradingSpace {
    //! The trader class will be the main class to interact with the market
    class Trader {

        public:
            Trader(Account& acc);
            //! Buy or sell a certain amount of a chosen good
            virtual void buy(Good& g, int amount);
            virtual void sell(Good& g, int amount);
        

        private:
            Account account;
    };
  
    
}; // namespace TradingSpace
