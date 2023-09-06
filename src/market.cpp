#include <market.hpp>

namespace TradingSpace {

    Market::Market() {
        Good bricks("Bricks", 1, 1.2, 0.5, 0.7);
        Good oil("Oil", 10, 0.2, 0.5, 0.3);
        Good wood("Wood", 5, 1.8, 0.5, 0.9);
        Good iron("Iron", 3, 1.6, 0.5, 0.1);
        Good gas("Gas", 0.5, 0.6, 0.5, 0.2);
        Good chemicals("Chemicals", 15, 1.2, 0.5, 0.8);

        goods.insert({"Bricks", bricks});
        goods.insert({"Oil",oil});
        goods.insert({"Wood", wood});
        goods.insert({"Iron", iron});
        goods.insert({"Gas", gas});
        goods.insert({"Chemicals", chemicals});
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

    std::unordered_set<Trader, TraderHash>& Market::get_traders() const{
        return traders;
    }

    std::unordered_map<std::string, Good>& Market::get_goods() const{
        return goods;
    }

    /**
     * GETTER AND SETTER
    */

} // namespace TradingSpace
