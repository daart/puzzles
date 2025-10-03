def bestTime(nums):
    min_price = float('inf')
    max_profit = 0

    for price in nums:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit