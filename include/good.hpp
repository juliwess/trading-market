#pragma once
#include <string>



namespace TradingSpace {
    //! @brief The Goods can be bought and sold in the market 
    class Good {
        public:
            /**
             *  The constructor gets a number of values that are used for the random-walk
            */
            Good(std::string name, float start_value, float tendency,
            float step_size, float average_change);

            /**
             * GETTER AND SETTER
            */
            virtual void set_value(const float& value);
            virtual float get_value() const;

            virtual std::string get_name() const;

            /**
             * GETTER AND SETTER
            */

            //! Function that will later refresh the goods value
            void adapt();

            bool operator<(const Good& other) const;
            
        private:
            //!Each good comes with a name
            std::string name;
            //! The market-value of a good
            float value;

            //!Variables used for the random-walk
            float tendency;
            float step_size;
            float average_change;
    };

}; // namespace TradingSpace
