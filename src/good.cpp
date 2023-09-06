#include <good.hpp>
#include <cmath>
#include <cstdlib>
#include <iostream>
namespace TradingSpace {

    

    Good::Good(std::string name, float start_value, float tendency,
    float step_size, float average_change)
     : name(name), value(start_value), tendency(tendency), step_size(step_size), average_change(average_change)
    {}

    //!Implementation of a random walk that generates the current value of the product
    void Good::adapt(){

        //Generates a random number between -1 and 1
        float rand = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX / 2) - 1.0f;

        //Refreshes the value using a random-walk
         value = value * (1 + average_change * step_size + average_change * sqrt(step_size) * rand);
    }

    /**
     * Getter and setter
     **/
    void Good::set_value(const float& value) {
        this->value = value;
    }

    float Good::get_value() const{
        return value;
    }

    std::string Good::get_name()const {
        return name;
    }

    /**
     * Getter and setter
     **/

    bool Good::operator<(const Good& other) const {
        return value < other.get_value();
    }
    
} // namespace TradingSpace
