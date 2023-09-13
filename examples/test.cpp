#include <market.hpp>
#include <good.hpp>
#include <trader.hpp>
#include <account.hpp>
#include <iostream>
#include <set>
#include <cstddef>
#include <functional>
#include <thread>
#include <chrono>
#include <fstream>

int main() {
    float r = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
    float r2 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
    float r3 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
    float r4 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
    float r5 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
    float r6 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
    float r7 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
    float r8 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));
    float r9 = -1 + static_cast <float> (std::rand()) /( static_cast <float> (RAND_MAX/(1+1)));

    std::cout<< r;
    std::cout<< "\n" << r2 <<"\n" << r3;


}