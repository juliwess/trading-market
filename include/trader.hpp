#pragma once
#include <account.hpp>
#include <good.hpp>
#include <unordered_map>

namespace TradingSpace {

    
    //! @brief The trader class will be the main class to interact with the market
    class Trader {
        public:
            Trader();
            //! Buy or sell a certain amount of a chosen good
            virtual void buy(const Good& g, int amount);
            virtual void sell(const Good& g, int amount);

            //! The Trader class will also implement a set_balance, deposit and withdraw function to avoid complications
            // when using the function in python
            virtual void set_balance(const float& bal);
            virtual void withdraw(const float& amount);
            virtual void deposit(const float& amount);

            //! Checks wether the entered password is correct
            virtual bool validate(std::string pw);

            /**
             *  Getter and setter
             **/
            virtual Account& get_account();
            virtual void set_account(Account& acc);

            virtual int get_id() const;
            virtual void set_id(int& id);

            virtual int get_instances() const;

            virtual int get_pw() const;
            virtual void set_pw(std::string pw);

            virtual std::unordered_map<std::string, int>& get_traders_goods();
            /**
             *  Getter and setter
             **/

            //! The Trader-Class will implement the opeartor== to use the unordered set
            bool operator==(const Trader& other) const;

        private:
            Account account;
            int id;

            int pw;
            //! Traders_goods saves the amount a trader's got of each individual good
            std::unordered_map<std::string, int> traders_goods;

            //! The instances of traders will be count in a public variable to generate a unique ID
            static int instances;
    };

    //! @brief An object of this class will later be used to create an unordered set of traders 
    class TraderHash {
        public:
            size_t operator() (const Trader& t) const;
    };
  
    
}; // namespace TradingSpace
