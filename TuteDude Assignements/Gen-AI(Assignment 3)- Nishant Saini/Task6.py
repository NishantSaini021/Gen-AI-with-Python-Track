# Task 6. Combines utility function

def process_prices(prices):
    dicounted_prices = list(map(lambda x: x - x*0.1, prices))
    filtered_prices = filter(lambda x: x > 300, dicounted_prices)
    print(f"Dicounted Prices: {list(dicounted_prices)}")
    print(f"Filtered Prices: {list(filtered_prices)}")

prices = [100,500,900,50,750]
process_prices(prices)