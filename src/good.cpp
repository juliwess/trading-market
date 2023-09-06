#include <good.hpp>
#include <cmath>
#include <cstdlib>
#include <iostream>
namespace TradingSpace {

    /**
     * GoodHash object will be used to implement an unordered_map that uses Goods as Keys
    */
    size_t GoodHash::operator()(const Good& g) const {
        return std::hash<int>{}(g.get_id());
    }
    

    Good::Good(int id, std::string name, float start_value, float tendency,
    float step_size, float average_change)
     : id(id), name(name), value(start_value), tendency(tendency), step_size(step_size), average_change(average_change)
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

    int Good::get_id() const {
        return id;
    }

    /**
     * Getter and setter
     **/


    /**
     * OPERATOR
    */
    bool Good::operator<(const Good& other) const {
        return value < other.get_value();
    }
    bool Good::operator==(const Good& other) const {
        return value == other.get_value();
    }
    /**
     * OPERATOR
    */
} // namespace TradingSpace
