#pragma once


namespace TradingSpace {
    //! @brief each Trader will posses one account to manage his balance of the fictive currency
    class Account {
        public:
            Account();
            Account(const float& start_balance);
            virtual void withdraw(const float& amount);
            virtual void deposit(const float& amount);
        private:
            float balance;
    };
}; // namespace TradingSpace
