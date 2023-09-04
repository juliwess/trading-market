#include <gtest/gtest.h>
#include <iostream>

TEST(MEINTEST, KeineNachrichten) {
    EXPECT_EQ(0,1)<<"1 ist nicht 1";
}