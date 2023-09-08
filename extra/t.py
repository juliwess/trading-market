from market import Market
from trader import Trader
from account import Account
from good import Good


def main():
    t = Trader()
    print(t.get_pw())
    t.set_pw("JULI")
    print(t.get_pw())


if __name__ == '__main__':
    main()