#Task 1. Basic Function: Price after duscount
def apply_function(price, discount_percent = 5):
    return (price) - ((discount_percent*price)/100)

print(apply_function(1000,10))
print(apply_function(500))
