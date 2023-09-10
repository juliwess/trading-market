#pragma once


namespace TradingSpace {
    //! @brief each Trader will posses one account to manage his balance of the fictive currency
    class Account {
        public:
            //! An account can either be created with a balance of 0 or a chosen balance
            Account();
            Account(const float& start_balance);

            //! Deposit and withdraw money
            virtual void withdraw(const float& amount);
            virtual void deposit(const float& amount);

            //! Getters and setters
            virtual float get_balance() const;
            virtual void set_balance(const float& bal);
        private:
            float balance;
    };
}; // namespace TradingSpace
