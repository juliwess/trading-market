#pragma once
#include <string>



namespace TradingSpace {
    //! @author Julian Wessling
    //! @brief The Goods can be bought and sold in the market 
    class Good {
        public:
            /*The constructor gets a number of values that are used for the random-walk*/
            Good(std::string name, float start_value, float tendency,
            float step_size, float average_change);
            void set_value(const float& value);
            float get_value();

            //! Function that will later refresh the goods value
            void adapt();
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
