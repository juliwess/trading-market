


namespace TradingSpace {
    
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
