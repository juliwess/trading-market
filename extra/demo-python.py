from market import Market
from trader import Trader
from good import Good

def main():
    foo = Market()
    foo2 = Trader()
    foo.addTrader(foo2)

    g = Good(1, "Bricks", 0.5, 0.5, 0.7, 0.1)
    foo2.buy(g, 3)
    print(g.get_name())


if __name__ == '__main__':
    main()