def best_time_to_buy_sell_stonks(nums):
    min_price = float('inf')
    max_profit = 0

    for price in nums:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit