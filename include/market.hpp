#pragma once
#include <trader.hpp>
#include <unordered_set>

namespace TradingSpace {
    class Market {
        public:
            Market();
            //! Add and remove traders from the market
            void addTrader(Trader& trader);
            void removeTrader(Trader& trader);
        private:
            std::unordered_set<Trader, TraderHash> traders;

    };
} // namespace TradingSpace
