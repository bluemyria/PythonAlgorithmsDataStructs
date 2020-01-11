from test_framework import generic_test

# 5.6 Buy and Sell a Stock Once
# Write a program that takes an array denoting the daily stock price,
# and returns the maximum profit that could be made by buying and then
# selling one share of that stock. There is no need to buy if no profit
# is possible
def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    # SOS!!! how do you use "infinite"
    # float('inf')
    # SOS usage of min() and max()
    min_so_far = float('inf')
    max_diff_so_far = 0
    
    for price in prices:
        min_so_far = min(min_so_far, price)
        max_diff_so_far = max(max_diff_so_far, price-min_so_far)
        print(price, min_so_far, max_diff_so_far)
    return max_diff_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
