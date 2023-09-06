#pragma once
#include <trader.hpp>
#include <unordered_set>

namespace TradingSpace {
    class Market {
        public:
            Market();

            //! Add and remove traders from the market
            virtual void addTrader(Trader& trader);
            virtual void removeTrader(Trader& trader);

            //! Getter and setter
            virtual std::unordered_set<Trader, TraderHash> get_traders();


        private:
            std::unordered_set<Trader, TraderHash> traders;

    };
} // namespace TradingSpace
