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

            /**
             *  Getter and setter
             **/
            virtual Account get_account() const;
            virtual void set_account(Account& acc);

            virtual int get_id() const;
            virtual void set_id(int& id);

            virtual int get_instances() const;
            /**
             *  Getter and setter
             **/

            //! The Trader-Class will implement the opeartor== to use the unordered set
            bool operator==(const Trader& other) const;

        private:
            Account account;
            int id;

            static int instances;
    };

    //! An object of this class will later be used to create an unordered set of traders 
    class TraderHash {
        public:
            size_t operator() (const Trader& t) const;
    };
  
    
}; // namespace TradingSpace
