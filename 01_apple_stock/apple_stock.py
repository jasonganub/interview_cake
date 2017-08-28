# Using the greedy algorithm
# Note: Always try greedy algorithm first

def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError("Need at least 2 values")

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday[1:]): # skip the first item, can't buy and sell same time
        potential_profit = current_price - min_price
        max_profit = max(potential_profit, max_profit)

        min_price = min(current_price, min_price)
        # could also use manual conditionals as well

    return max_profit


# run your function through some test cases here
# remember: debugging is half the battle!
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices_yesterday))
