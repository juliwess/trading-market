#include <account.hpp>

namespace TradingSpace {

   Account::Account() {
        balance = 0;
   }

   Account::Account(const float& start_balance) {
        balance = start_balance;
   }
   
   /**
    * Whenever a trader decides to buy or sell assets his balance will
    * be updated
   */
   void Account::deposit(const float& amount) {
        balance += amount;
   }

   void Account::withdraw(const float& amount) {
        balance -= amount;
   }
} // namespace TradingSpace
