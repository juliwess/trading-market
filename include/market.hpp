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

            virtual void update_values();

            /**
             * Getter and setter
             */ 
            virtual std::unordered_map<int, Trader>& get_traders();

            virtual std::unordered_map<std::string, Good>& get_goods();

            virtual void set_trader_password(int id, std::string pw);

            virtual Trader& get_trader_by_id(int id);
            /**
             * Getter and setter
             */ 


        private:
            std::unordered_map<int, Trader> traders;
            std::unordered_map<std::string, Good> goods;
    };
} // namespace TradingSpace
