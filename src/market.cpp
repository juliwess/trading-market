#include <market.hpp>

namespace TradingSpace {

    Market::Market() {

    }

    void Market::addTrader(Trader& trader) {
        traders.insert(trader);
    }

    void Market::removeTrader(Trader& trader) {
        traders.erase(trader);
    }


    /**
     * GETTER AND SETTER
    */

    std::unordered_set<Trader, TraderHash> Market::get_traders() {
        return traders;
    }

    /**
     * GETTER AND SETTER
    */

} // namespace TradingSpace
