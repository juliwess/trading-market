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

            //! Getter and setter
            virtual std::unordered_set<Trader, TraderHash>& get_traders() const;

            virtual std::unordered_map<std::string, Good>& get_goods() const;

        private:
            std::unordered_set<Trader, TraderHash> traders;
            std::unordered_map<std::string, Good> goods;
    };
} // namespace TradingSpace
