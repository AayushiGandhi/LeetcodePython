def maxProfit(prices):
    buy = 0
    sell = 1
    max_profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            if max_profit < profit:
                max_profit = profit
            sell += 1
        else:
            buy = sell
            sell += 1
    return max_profit


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([1,2,3,4,5]))
