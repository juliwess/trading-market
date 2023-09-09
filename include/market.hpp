#pragma once
#include <trader.hpp>
#include <good.hpp>
#include <unordered_map>
#include <unordered_set>

namespace TradingSpace {
    class Market {
        public:
            Market();

            //! Add and remove traders from the market
            virtual void addTrader(Trader& trader);
            virtual void removeTrader(Trader& trader);
            virtual void removeTraderById(int id);

            //!Update the prices for each good
            virtual void update_values();

            //! Lets the trader buy goods
            virtual void trader_buy(int id, std::string good_name, int amount);

            /**
             * Getter and setter
             */ 
            virtual std::unordered_map<int, Trader>& get_traders();

            virtual std::unordered_map<std::string, Good>& get_goods();

            virtual void set_trader_password(int id, std::string pw);

            virtual Trader& get_trader_by_id(int id);

            virtual float get_traders_balance(int id);
            /**
             * Getter and setter
             */ 


        private:
            std::unordered_map<int, Trader> traders;
            std::unordered_map<std::string, Good> goods;
    };
} // namespace TradingSpace
