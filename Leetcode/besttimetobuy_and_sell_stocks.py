prices = [7, 1, 5, 3, 6, 4]
max_profit = 0 
min_price = float('inf')
for price in prices:
    if price < min_price:
        min_price = price
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit
return max_profit

#  max_profit = 0
#         min_price = float("inf")
#         n = len(prices)
#         for i in range(0, n):
#             min_price = min(min_price, prices[i])
#             max_profit = max(max_profit, prices[i] - min_price)
#         return max_profit