# using map(): Apply gst to list of prices

prices = [100,250,400,1200,500]
gst = lambda price: price + 0.18*price
prices_after_gst = map(gst, prices)

print(f"Prices bofre GST: {prices}")
print(f"Prices after GST: {list(prices_after_gst)}")